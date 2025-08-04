import cv2
import mediapipe as mp

# สร้างอ็อบเจกต์สำหรับ face detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# ใช้กล้อง
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("ไม่สามารถอ่านภาพจากกล้องได้")
            break

        # แปลง BGR -> RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ปรับปรุงประสิทธิภาพ
        image.flags.writeable = False
        results = face_detection.process(image)

        # กลับมาเป็น writeable เพื่อแสดงผล
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # วาดกรอบใบหน้า
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        # แสดงผลภาพ
        cv2.imshow('MediaPipe Face Detection', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
