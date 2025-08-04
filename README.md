# Python MediaPipe Face Recognition Project

## ภาพรวม

โปรเจคนี้เป็นระบบ Face Recognition และ Liveness Detection ที่พัฒนาด้วย Python โดยใช้ MediaPipe และ face_recognition library มีทั้ง Command Line Interface และ Web Interface

## ฟีเจอร์หลัก

### 🎯 Face Recognition (main.py)
- **การจดจำใบหน้าหลายคน** - โหลดรูปจากโฟลเดอร์ `known_people/`
- **แสดงร้อยละความเหมือน** - แสดงความแม่นยำในการจดจำ
- **Real-time Processing** - ประมวลผลแบบ real-time จากกล้อง
- **สีกรอบตามสถานะ** - สีเขียวสำหรับคนที่รู้จัก, สีแดงสำหรับคนไม่รู้จัก

### 🌐 Web Interface (app.py)
- **Liveness Detection** - ตรวจจับการกระพริบตาและยิ้ม
- **Modern UI** - ออกแบบสวยงามและใช้งานง่าย
- **Thai Language Support** - แสดงข้อความภาษาไทยได้ถูกต้อง
- **Real-time Updates** - อัปเดตสถานะแบบ real-time
- **Responsive Design** - รองรับทุกขนาดหน้าจอ

## โครงสร้างโปรเจค

```
py_Mediapipe/
├── README.md              # เอกสารหลักของโปรเจค
├── main.py                # Face Recognition (Command Line)
├── app.py                 # Web Interface (Flask)
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── known_people/         # ไฟล์ภาพใบหน้าที่รู้จัก
│   ├── yui.jpg          # ภาพตัวอย่าง
│   ├── john.png         # เพิ่มคนอื่นๆ ได้
│   └── mary.jpeg        # รองรับหลายรูปแบบไฟล์
├── templates/           # Web templates
│   └── index.html      # Web interface
├── venv310/            # Python virtual environment (Python 3.10)
└── docs/               # เอกสารและบันทึกการทำงาน
    ├── project_structure.md      # โครงสร้างโปรเจค
    ├── face_recognition_updates.md # การอัปเดต face recognition
    ├── web_interface_guide.md    # คู่มือ Web Interface
    ├── python_path_info.md       # ข้อมูล Python paths
    ├── gitignore_info.md         # ข้อมูล .gitignore
    └── git_setup_info.md         # การตั้งค่า Git
```

## เอกสารเพิ่มเติม
- [โครงสร้างโปรเจค](docs/project_structure.md) - รายละเอียดโครงสร้างและไฟล์
- [การอัปเดต Face Recognition](docs/face_recognition_updates.md) - การเปลี่ยนแปลงระบบจดจำใบหน้า
- [คู่มือ Web Interface](docs/web_interface_guide.md) - การใช้งาน Web Interface
- [ข้อมูล Python Paths](docs/python_path_info.md) - การหาพาธ Python และสร้าง virtual environment
- [ข้อมูล Gitignore](docs/gitignore_info.md) - การตั้งค่า .gitignore
- [การตั้งค่า Git](docs/git_setup_info.md) - คำสั่ง Git พื้นฐาน

## การติดตั้งและใช้งาน

### 1. การตั้งค่า Environment
```bash
# สร้าง virtual environment
python -m venv venv310

# เปิดใช้งาน virtual environment
source venv310/bin/activate  # macOS/Linux
# หรือ venv310\Scripts\activate  # Windows

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### 2. การใช้งาน Face Recognition (Command Line)
```bash
# รัน Face Recognition
python main.py

# วิธีใช้งาน:
# - กด ESC เพื่อออกจากโปรแกรม
# - ใส่รูปคนในโฟลเดอร์ known_people/
# - ระบบจะแสดงชื่อและร้อยละความเหมือน
```

### 3. การใช้งาน Web Interface
```bash
# รัน Web Server
python app.py

# เข้าใช้งาน:
# - http://localhost:8080
# - กระพริบตาหรือยิ้มเพื่อผ่านการตรวจสอบ
```

## ข้อมูลสำคัญ

### 1. ไฟล์หลัก
- **main.py**: Face Recognition ด้วย `face_recognition` library
  - โหลดภาพจาก `known_people/` (รองรับหลายคน)
  - แสดงร้อยละความเหมือน (0-100%)
  - ใช้เกณฑ์ 0.6 ในการตัดสิน

- **app.py**: Web Interface ด้วย Flask + MediaPipe
  - Liveness Detection (กระพริบตา/ยิ้ม)
  - Real-time status updates
  - Modern responsive UI

### 2. Dependencies หลัก
```txt
face-recognition==1.3.0    # Face recognition
mediapipe==0.10.21        # Face detection & landmarks
opencv-python==4.12.0.88  # Image processing
Flask==3.1.1              # Web framework
flask-cors==4.0.0         # CORS support
dlib==20.0.0              # Face recognition dependency
```

### 3. การเพิ่มคนในระบบ
1. ใส่รูปคนในโฟลเดอร์ `known_people/`
2. รองรับไฟล์: `.jpg`, `.png`, `.jpeg`, `.bmp`, `.tiff`
3. ใช้ชื่อไฟล์เป็นชื่อคน (ไม่รวมนามสกุล)
4. รันโปรแกรมใหม่ - ระบบจะโหลดอัตโนมัติ

### 4. การปรับแต่ง
- **เกณฑ์ความเหมือน**: แก้ไขใน `main.py` (ค่า 0.6)
- **เกณฑ์ Liveness**: แก้ไขใน `app.py` (การกระพริบตา/ยิ้ม)
- **Port**: แก้ไขใน `app.py` (ค่า 8080)
- **UI**: แก้ไขใน `templates/index.html`

## ฟีเจอร์ที่กำลังพัฒนา

- [ ] การบันทึกผลการตรวจสอบ
- [ ] การปรับแต่งเกณฑ์แบบ real-time
- [ ] การเพิ่ม/ลบคนในระบบผ่าน Web UI
- [ ] การส่งแจ้งเตือนเมื่อพบคนที่ไม่รู้จัก
- [ ] การแสดงสถิติการใช้งาน

## การแก้ไขปัญหา

### ปัญหาที่พบบ่อย
1. **Port 5000 ถูกใช้งาน** → เปลี่ยนเป็น 8080
2. **ข้อความภาษาไทยเป็นสี่เหลี่ยม** → ใช้ Web Interface แทน
3. **การเชื่อมต่อถูกตัด** → ตรวจสอบ CORS และ dependencies
4. **กล้องไม่ทำงาน** → ตรวจสอบสิทธิ์การเข้าถึงกล้อง

### การทดสอบ
```bash
# ทดสอบการเชื่อมต่อ
curl http://localhost:8080/test

# ทดสอบ dependencies
python -c "import face_recognition, mediapipe, cv2, flask; print('All OK')"
```

## สำหรับ AI ตัวถัดไป

โปรเจคนี้เป็นตัวอย่างการใช้งาน Computer Vision สำหรับ Face Recognition และ Liveness Detection โดยมีฟีเจอร์ที่ครบครัน:

### ข้อควรระวัง:
- การติดตั้ง dlib อาจมีปัญหาในบางระบบ
- ต้องมีกล้องที่ใช้งานได้
- ภาพใน known_people ควรมีคุณภาพดีและมีใบหน้าที่ชัดเจน
- ใช้ port 8080 แทน 5000 เพื่อหลีกเลี่ยงการขัดแย้งกับ AirPlay

### การพัฒนาต่อ:
- เพิ่มฟีเจอร์การบันทึกและวิเคราะห์
- ปรับปรุงประสิทธิภาพการประมวลผล
- เพิ่มการรองรับการใช้งานแบบ distributed
- พัฒนา mobile app หรือ desktop app
