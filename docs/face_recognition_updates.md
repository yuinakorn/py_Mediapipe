# Face Recognition Updates

## การอัปเดตล่าสุด (5 สิงหาคม 2025)

### 1. การแสดงร้อยละความเหมือน (Percentage Display)

**การเปลี่ยนแปลง:**
- เปลี่ยนจากการใช้ `face_recognition.compare_faces()` เป็น `face_recognition.face_distance()`
- แสดงร้อยละความเหมือนแทนการแสดงผลแบบ boolean
- ใช้เกณฑ์ 0.6 เป็นเกณฑ์มาตรฐานในการตัดสิน

**โค้ดที่เปลี่ยนแปลง:**
```python
# เดิม - ใช้ boolean
matches = face_recognition.compare_faces(known_encodings, face_encoding)
if True in matches:
    name = known_names[matches.index(True)]

# ใหม่ - ใช้ระยะห่างและร้อยละ
face_distances = face_recognition.face_distance(known_encodings, face_encoding)
best_match_index = face_distances.argmin()
similarity_percentage = (1 - face_distances[best_match_index]) * 100

if face_distances[best_match_index] < 0.6:
    name = known_names[best_match_index]
else:
    name = "Unknown"
```

**ผลลัพธ์:**
- แสดงชื่อพร้อมร้อยละ เช่น "Yui (85.2%)" หรือ "Unknown (45.1%)"
- ความแม่นยำในการจดจำดีขึ้น
- สามารถปรับเกณฑ์ได้ตามต้องการ

### 2. การรองรับหลายคน (Multiple People Support)

**การเปลี่ยนแปลง:**
- โหลดรูปทั้งหมดในโฟลเดอร์ `known_people/` แทนการโหลดไฟล์เดียว
- รองรับไฟล์ `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`
- ใช้ชื่อไฟล์เป็นชื่อคน

**โค้ดใหม่:**
```python
known_encodings = []
known_names = []

if os.path.exists("known_people"):
    for filename in os.listdir("known_people"):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            name = os.path.splitext(filename)[0]
            image_path = os.path.join("known_people", filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            
            if len(face_encodings) > 0:
                known_encodings.append(face_encodings[0])
                known_names.append(name)
```

**วิธีใช้งาน:**
1. ใส่รูปคนในโฟลเดอร์ `known_people/` เช่น:
   - `yui.jpg`
   - `john.png`
   - `mary.jpeg`
2. รันโปรแกรม - จะโหลดทุกคนอัตโนมัติ
3. แสดงผลพร้อมร้อยละความเหมือน

### 3. Web Interface ด้วย Flask

**ฟีเจอร์ใหม่:**
- สร้าง web interface ด้วย Flask
- แสดงข้อความภาษาไทยใน HTML แทนการวาดบนวิดีโอ
- ใช้ Server-Sent Events สำหรับ real-time updates
- UI สวยงามและ responsive

**ไฟล์ที่เพิ่ม:**
- `app.py` - Flask web application
- `templates/index.html` - Web interface
- `requirements.txt` - เพิ่ม Flask dependencies

**ฟีเจอร์หลัก:**
- **Liveness Detection** - ตรวจจับการกระพริบตาและยิ้ม
- **Real-time Status** - อัปเดตสถานะแบบ real-time
- **Thai Language Support** - แสดงข้อความภาษาไทยได้ถูกต้อง
- **Responsive Design** - รองรับทุกขนาดหน้าจอ

**การใช้งาน:**
```bash
# รัน web server
python app.py

# เข้าใช้งาน
http://localhost:8080
```

### 4. การแก้ไขปัญหา

**ปัญหา:**
- ข้อความภาษาไทยแสดงเป็นสี่เหลี่ยมบนวิดีโอ
- การเชื่อมต่อถูกตัดใน web interface
- JSON serialization error

**การแก้ไข:**
1. **ภาษาไทยในวิดีโอ** - ย้ายไปแสดงใน HTML แทน
2. **การเชื่อมต่อ** - เพิ่ม CORS support และเปลี่ยน port เป็น 8080
3. **JSON Error** - เปลี่ยน boolean เป็น integer

### 5. Dependencies ที่เพิ่ม

```txt
Flask==3.1.1
flask-cors==4.0.0
mediapipe==0.10.21
```

### 6. โครงสร้างไฟล์ใหม่

```
py_Mediapipe/
├── main.py                # Face Recognition (Command Line)
├── app.py                 # Web Interface (Flask)
├── templates/
│   └── index.html        # Web UI
├── known_people/         # รูปหลายคน
│   ├── yui.jpg
│   ├── john.png
│   └── mary.jpeg
└── requirements.txt      # Dependencies
```

### 7. ฟีเจอร์ที่กำลังพัฒนา

- [ ] การบันทึกผลการตรวจสอบ
- [ ] การปรับแต่งเกณฑ์ความเหมือน
- [ ] การเพิ่ม/ลบคนในระบบ
- [ ] การส่งแจ้งเตือนเมื่อพบคนที่ไม่รู้จัก

## สรุป

การอัปเดตครั้งนี้ทำให้ระบบ face recognition มีความสามารถมากขึ้น:
- แสดงร้อยละความเหมือนที่แม่นยำ
- รองรับการจดจำหลายคน
- มี web interface ที่ใช้งานง่าย
- แก้ไขปัญหาการแสดงผลภาษาไทย
- เพิ่มความเสถียรในการทำงาน 