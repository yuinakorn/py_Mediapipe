import face_recognition
import cv2
import os

# โหลดภาพใบหน้าที่รู้จักทั้งหมดในโฟลเดอร์
known_encodings = []
known_names = []

# ตรวจสอบว่าโฟลเดอร์ known_people มีอยู่หรือไม่
if os.path.exists("known_people"):
    # วนลูปผ่านไฟล์ทั้งหมดในโฟลเดอร์
    for filename in os.listdir("known_people"):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # เอานามสกุลไฟล์ออกเพื่อใช้เป็นชื่อ
            name = os.path.splitext(filename)[0]
            
            try:
                # โหลดภาพและสร้าง encoding
                image_path = os.path.join("known_people", filename)
                image = face_recognition.load_image_file(image_path)
                face_encodings = face_recognition.face_encodings(image)
                
                if len(face_encodings) > 0:
                    # ใช้ใบหน้าแรกที่พบในภาพ
                    known_encodings.append(face_encodings[0])
                    known_names.append(name)
                    print(f"Loaded image for {name} successfully")
                else:
                    print(f"No face found in {filename}")
                    
            except Exception as e:
                print(f"Error loading {filename}: {e}")
else:
    print("known_people folder not found")

print(f"Loaded {len(known_names)} people: {', '.join(known_names)}")

# เปิดกล้อง
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ย่อภาพให้เล็กลงเพื่อให้เร็วขึ้น
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # หาตำแหน่งใบหน้า
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # คำนวณระยะห่างระหว่างใบหน้า
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = face_distances.argmin()
        
        # คำนวณร้อยละความเหมือน (0.6 เป็นเกณฑ์มาตรฐาน)
        similarity_percentage = (1 - face_distances[best_match_index]) * 100
        
        if face_distances[best_match_index] < 0.6:
            name = known_names[best_match_index]
            color = (0, 255, 0)  # สีเขียว (BGR)
        else:
            name = "Unknown"
            color = (0, 0, 255)  # สีแดง (BGR)

        # ขยายกรอบให้ตรงกับขนาดภาพจริง
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # วาดกรอบใบหน้าและชื่อพร้อมร้อยละ
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        
        # แสดงชื่อและร้อยละความเหมือน
        display_text = f"{name} ({similarity_percentage:.1f}%)"
        cv2.putText(frame, display_text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # กด ESC เพื่อออก
        break

cap.release()
cv2.destroyAllWindows()
