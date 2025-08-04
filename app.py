from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)

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

def eye_aspect_ratio(landmarks, eye_pts):
    p1 = np.array([landmarks[eye_pts[0]].x, landmarks[eye_pts[0]].y])
    p2 = np.array([landmarks[eye_pts[1]].x, landmarks[eye_pts[1]].y])
    return np.linalg.norm(p2 - p1)

def find_thai_font(font_size=32):
    """หาฟอนต์ที่รองรับภาษาไทย"""
    # รายการฟอนต์ที่รองรับภาษาไทย (เรียงตามลำดับความน่าจะเป็น)
    thai_fonts = [
        # macOS
        "/System/Library/Fonts/Supplemental/Thonburi.ttc",
        "/System/Library/Fonts/Supplemental/Ayuthaya.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        # Windows
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/tahoma.ttf",
        # Google Fonts (ถ้ามี)
        "/usr/share/fonts/truetype/google/noto/NotoSansThai-Regular.ttf",
    ]
    
    for font_path in thai_fonts:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, font_size)
            except:
                continue
    
    # ถ้าไม่พบฟอนต์ภาษาไทย ให้ใช้ฟอนต์เริ่มต้น
    return ImageFont.load_default()

def draw_text(image, text, position, font_size=32, color=(0, 255, 0), use_thai=True):
    """วาดข้อความบนภาพ"""
    # แปลง OpenCV image เป็น PIL Image
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    draw = ImageDraw.Draw(pil_image)
    
    if use_thai:
        # ลองใช้ฟอนต์ภาษาไทย
        font = find_thai_font(font_size)
        # ทดสอบว่าฟอนต์รองรับภาษาไทยหรือไม่
        try:
            # ทดสอบวาดตัวอักษรไทย
            test_text = "ทดสอบ"
            draw.text((0, 0), test_text, font=font, fill=(0, 0, 0))
            # ถ้าสำเร็จ ใช้ภาษาไทย
            language = 'th'
        except:
            # ถ้าไม่สำเร็จ ใช้ภาษาอังกฤษ
            language = 'en'
    else:
        font = ImageFont.load_default()
        language = 'en'
    
    # เลือกข้อความตามภาษา
    if text in MESSAGES:
        display_text = MESSAGES[text][language]
    else:
        display_text = text
    
    # วาดข้อความ
    draw.text(position, display_text, font=font, fill=color)
    
    # แปลงกลับเป็น OpenCV format
    image_bgr = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return image_bgr

def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        message_key = 'no_face'

        if result.multi_face_landmarks:
            for landmarks in result.multi_face_landmarks:
                h, w, _ = frame.shape
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

                mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_TESSELATION)

        # แสดงข้อความ
        frame = draw_text(frame, message_key, (30, 50), font_size=32, color=(0, 255, 0), use_thai=True)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
