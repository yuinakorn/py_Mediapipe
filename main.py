import face_recognition
import cv2
import os

# โหลดภาพใบหน้าที่รู้จัก
known_image = face_recognition.load_image_file("known_people/yui.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]
known_names = ["Yui"]
known_encodings = [known_encoding]

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
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        # ขยายกรอบให้ตรงกับขนาดภาพจริง
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # กำหนดสีตามชื่อ
        if name == "Unknown":
            color = (0, 0, 255)  # สีแดง (BGR)
        else:
            color = (0, 255, 0)  # สีเขียว (BGR)

        # วาดกรอบใบหน้าและชื่อ
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # กด ESC เพื่อออก
        break

cap.release()
cv2.destroyAllWindows()
