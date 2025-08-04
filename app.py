from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import cv2
import mediapipe as mp
import numpy as np
import json
import threading
import time

app = Flask(__name__)
CORS(app)  # เพิ่ม CORS support

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# สำหรับ Liveness
LEFT_EYE = [33, 159]
RIGHT_EYE = [362, 386]
MOUTH = [61, 291]

# ข้อความภาษาไทยและภาษาอังกฤษ
MESSAGES = {
    'no_face': {'th': 'ยังไม่พบใบหน้า', 'en': 'No face detected'},
    'blinking': {'th': 'กระพริบตาแล้ว ✅', 'en': 'Blinking detected ✅'},
    'smiling': {'th': 'ยิ้มแล้ว ✅', 'en': 'Smiling detected ✅'},
    'waiting': {'th': 'โปรดกระพริบตาหรือยิ้ม...', 'en': 'Please blink or smile...'}
}

# ตัวแปรสำหรับเก็บสถานะปัจจุบัน
current_status = {
    'message_key': 'no_face',
    'message_th': MESSAGES['no_face']['th'],
    'message_en': MESSAGES['no_face']['en'],
    'has_face': 0,  # เปลี่ยนจาก False เป็น 0
    'is_blinking': 0,  # เปลี่ยนจาก False เป็น 0
    'is_smiling': 0  # เปลี่ยนจาก False เป็น 0
}

def eye_aspect_ratio(landmarks, eye_pts):
    p1 = np.array([landmarks[eye_pts[0]].x, landmarks[eye_pts[0]].y])
    p2 = np.array([landmarks[eye_pts[1]].x, landmarks[eye_pts[1]].y])
    return np.linalg.norm(p2 - p1)

def process_frame(frame):
    """ประมวลผลเฟรมและอัปเดตสถานะ"""
    global current_status
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    message_key = 'no_face'
    status_data = {
        'message_key': message_key,
        'message_th': MESSAGES[message_key]['th'],
        'message_en': MESSAGES[message_key]['en'],
        'has_face': 0,  # เปลี่ยนจาก False เป็น 0
        'is_blinking': 0,  # เปลี่ยนจาก False เป็น 0
        'is_smiling': 0  # เปลี่ยนจาก False เป็น 0
    }

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            landmark_list = landmarks.landmark

            # ตรวจตา
            left_eye_open = eye_aspect_ratio(landmark_list, LEFT_EYE)
            right_eye_open = eye_aspect_ratio(landmark_list, RIGHT_EYE)

            # ตรวจยิ้ม (ระยะปาก)
            mouth_width = eye_aspect_ratio(landmark_list, MOUTH)

            # เช็ค liveness
            is_blinking = left_eye_open < 0.01 and right_eye_open < 0.01
            is_smiling = mouth_width > 0.08

            if is_blinking:
                message_key = 'blinking'
            elif is_smiling:
                message_key = 'smiling'
            else:
                message_key = 'waiting'

            status_data = {
                'message_key': message_key,
                'message_th': MESSAGES[message_key]['th'],
                'message_en': MESSAGES[message_key]['en'],
                'has_face': 1,  # เปลี่ยนจาก True เป็น 1
                'is_blinking': 1 if is_blinking else 0,  # เปลี่ยนจาก boolean เป็น integer
                'is_smiling': 1 if is_smiling else 0  # เปลี่ยนจาก boolean เป็น integer
            }
            
            # วาด landmarks บนเฟรม
            mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_TESSELATION)
            break

    # อัปเดตสถานะปัจจุบัน
    current_status = status_data
    return frame

def generate_frames():
    """สร้างวิดีโอสตรีม"""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("ไม่สามารถเปิดกล้องได้")
        return

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            # ประมวลผลเฟรมและอัปเดตสถานะ
            frame = process_frame(frame)

            # ส่งเฟรม
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            
            # หน่วงเวลาเล็กน้อย
            time.sleep(0.03)  # ~30 FPS
            
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในวิดีโอสตรีม: {e}")
    finally:
        cap.release()

def generate_status():
    """สร้างสถานะสตรีม"""
    while True:
        try:
            # ส่งสถานะปัจจุบัน
            yield f"data: {json.dumps(current_status)}\n\n"
            time.sleep(0.1)  # อัปเดตทุก 100ms
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในสถานะสตรีม: {e}")
            break

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status_feed')
def status_feed():
    return Response(generate_status(), mimetype='text/event-stream')

@app.route('/test')
def test():
    return jsonify({'status': 'OK', 'message': 'Server is running'})

if __name__ == '__main__':
    print("🚀 เริ่มต้นเซิร์ฟเวอร์...")
    print("📱 เข้าไปที่: http://localhost:8080")
    print("🔧 หรือ: http://127.0.0.1:8080")
    print("⏹️  กด Ctrl+C เพื่อหยุด")
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
