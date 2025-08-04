# Project Structure and Documentation

## โครงสร้างโปรเจคปัจจุบัน (5 สิงหาคม 2025)

```
py_Mediapipe/
├── README.md              # เอกสารหลักของโปรเจค
├── main.py                # Face Recognition (Command Line Interface)
├── app.py                 # Web Interface (Flask + MediaPipe)
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── known_people/         # ไฟล์ภาพใบหน้าที่รู้จัก
│   ├── yui.jpg          # ภาพตัวอย่าง
│   ├── john.png         # เพิ่มคนอื่นๆ ได้
│   └── mary.jpeg        # รองรับหลายรูปแบบไฟล์
├── templates/           # Web templates
│   └── index.html      # Web interface template
├── uploads/            # โฟลเดอร์สำหรับอัปโหลดไฟล์ (ถ้ามี)
├── venv310/           # Python virtual environment (Python 3.10)
└── docs/              # เอกสารและบันทึกการทำงาน
    ├── project_structure.md      # ไฟล์นี้
    ├── face_recognition_updates.md # การอัปเดต face recognition
    ├── web_interface_guide.md    # คู่มือ Web Interface
    ├── python_path_info.md       # ข้อมูล Python paths
    ├── gitignore_info.md         # ข้อมูล .gitignore
    └── git_setup_info.md         # การตั้งค่า Git
```

## การเปลี่ยนแปลงล่าสุด

### วันที่: 5 สิงหาคม 2025

**การเปลี่ยนแปลงหลัก:**
1. **เพิ่ม Web Interface** - สร้าง Flask application สำหรับ Liveness Detection
2. **ปรับปรุง Face Recognition** - เพิ่มการแสดงร้อยละความเหมือนและรองรับหลายคน
3. **แก้ไขปัญหา** - แก้ไขปัญหาการแสดงผลภาษาไทยและการเชื่อมต่อ
4. **เพิ่มเอกสาร** - สร้างคู่มือ Web Interface

**ไฟล์ที่เพิ่ม:**
- `app.py` - Flask web application
- `templates/index.html` - Web interface template
- `docs/web_interface_guide.md` - คู่มือ Web Interface

**ไฟล์ที่อัปเดต:**
- `main.py` - เพิ่มการแสดงร้อยละและรองรับหลายคน
- `requirements.txt` - เพิ่ม Flask dependencies
- `README.md` - อัปเดตให้ทันสมัย
- `docs/face_recognition_updates.md` - อัปเดตฟีเจอร์ใหม่

## ฟีเจอร์หลักของแต่ละไฟล์

### 1. main.py (Face Recognition)
- **เทคโนโลยี**: face_recognition library
- **ฟีเจอร์**:
  - โหลดรูปหลายคนจาก `known_people/`
  - แสดงร้อยละความเหมือน (0-100%)
  - สีกรอบตามสถานะ (เขียว/แดง)
  - Real-time processing

### 2. app.py (Web Interface)
- **เทคโนโลยี**: Flask + MediaPipe
- **ฟีเจอร์**:
  - Liveness Detection (กระพริบตา/ยิ้ม)
  - Real-time status updates
  - Server-Sent Events
  - CORS support

### 3. templates/index.html (Web UI)
- **เทคโนโลยี**: HTML5 + CSS3 + JavaScript
- **ฟีเจอร์**:
  - Responsive design
  - Thai language support
  - Real-time status display
  - Modern UI/UX

## Dependencies ที่ใช้

### Core Dependencies
```txt
face-recognition==1.3.0    # Face recognition
mediapipe==0.10.21        # Face detection & landmarks
opencv-python==4.12.0.88  # Image processing
dlib==20.0.0              # Face recognition dependency
numpy==2.2.6              # Numerical computing
```

### Web Dependencies
```txt
Flask==3.1.1              # Web framework
flask-cors==4.0.0         # CORS support
pillow==11.3.0            # Image processing (PIL)
```

## การใช้งาน

### Command Line Interface
```bash
# รัน Face Recognition
python main.py
```

### Web Interface
```bash
# รัน Web Server
python app.py

# เข้าใช้งาน
http://localhost:8080
```

## การพัฒนา

### 1. การเพิ่มคนในระบบ
1. ใส่รูปใน `known_people/`
2. รองรับ: `.jpg`, `.png`, `.jpeg`, `.bmp`, `.tiff`
3. ใช้ชื่อไฟล์เป็นชื่อคน

### 2. การปรับแต่ง
- **เกณฑ์ความเหมือน**: แก้ไขใน `main.py` (ค่า 0.6)
- **เกณฑ์ Liveness**: แก้ไขใน `app.py`
- **Port**: แก้ไขใน `app.py` (ค่า 8080)
- **UI**: แก้ไขใน `templates/index.html`

### 3. การแก้ไขปัญหา
- **Port 5000 ถูกใช้งาน** → เปลี่ยนเป็น 8080
- **ภาษาไทยเป็นสี่เหลี่ยม** → ใช้ Web Interface
- **การเชื่อมต่อถูกตัด** → ตรวจสอบ CORS

## วัตถุประสงค์ของโครงสร้าง

### 1. ความเป็นระเบียบ
- แยกเอกสารออกจากไฟล์โค้ดหลัก
- แยก Web Interface ออกจาก Command Line
- ง่ายต่อการค้นหาและจัดการ

### 2. การบำรุงรักษา
- เอกสารทั้งหมดอยู่ใน `docs/`
- โค้ดแยกตามหน้าที่ชัดเจน
- ง่ายต่อการอัปเดตและแก้ไข

### 3. การทำงานเป็นทีม
- AI ตัวถัดไปจะรู้โครงสร้างที่ชัดเจน
- เอกสารครบครันและทันสมัย
- ง่ายต่อการติดตามการเปลี่ยนแปลง

## สำหรับ AI ตัวถัดไป

### กฎการเขียนไฟล์ .md:
1. **ไฟล์ .md ใหม่ทั้งหมด** ให้เขียนในโฟลเดอร์ `docs/`
2. **README.md** ยังคงอยู่ที่ root directory
3. **ตั้งชื่อไฟล์** ให้สื่อความหมายและเป็นภาษาอังกฤษ
4. **เพิ่มลิงก์** ไปยังไฟล์ .md อื่นๆ ใน docs/ ถ้าจำเป็น

### ตัวอย่างการตั้งชื่อไฟล์:
- `docs/feature_updates.md` - การอัปเดตฟีเจอร์
- `docs/troubleshooting.md` - การแก้ไขปัญหา
- `docs/installation_guide.md` - คู่มือการติดตั้ง
- `docs/api_documentation.md` - เอกสาร API

### การอัปเดต README.md:
เมื่อเพิ่มไฟล์ .md ใหม่ใน docs/ ให้อัปเดต README.md เพื่อเพิ่มลิงก์ไปยังเอกสารใหม่

### หมายเหตุสำคัญ:
- ใช้ port 8080 แทน 5000 เพื่อหลีกเลี่ยงการขัดแย้งกับ AirPlay
- รองรับการแสดงผลภาษาไทยใน Web Interface
- มีการจัดการข้อผิดพลาดที่ครบครัน
- ใช้ Server-Sent Events สำหรับ real-time updates 