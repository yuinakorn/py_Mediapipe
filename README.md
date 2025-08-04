# Python MediaPipe Face Recognition Project

## โครงสร้างโปรเจค
```
py_Mediapipe/
├── README.md              # เอกสารหลักของโปรเจค
├── main.py                # Face Recognition ด้วย face_recognition library
├── app.py                 # Face Detection ด้วย MediaPipe
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── known_people/         # ไฟล์ภาพใบหน้าที่รู้จัก
│   └── yui.jpg          # ภาพตัวอย่าง
├── venv310/             # Python virtual environment (Python 3.10)
└── docs/                # เอกสารและบันทึกการทำงาน
    ├── project_structure.md      # โครงสร้างโปรเจค
    ├── python_path_info.md       # ข้อมูล Python paths
    ├── face_recognition_updates.md # การอัปเดต face recognition
    ├── gitignore_info.md         # ข้อมูล .gitignore
    └── git_setup_info.md         # การตั้งค่า Git
```

## เอกสารเพิ่มเติม
- [โครงสร้างโปรเจค](docs/project_structure.md) - รายละเอียดโครงสร้างและไฟล์
- [ข้อมูล Python Paths](docs/python_path_info.md) - การหาพาธ Python และสร้าง virtual environment
- [การอัปเดต Face Recognition](docs/face_recognition_updates.md) - การเปลี่ยนแปลงระบบจดจำใบหน้า
- [ข้อมูล Gitignore](docs/gitignore_info.md) - การตั้งค่า .gitignore
- [การตั้งค่า Git](docs/git_setup_info.md) - คำสั่ง Git พื้นฐาน

## ข้อมูลสำคัญ

### 1. การตั้งค่า Environment
- ใช้ Python virtual environment (venv) ตามที่ user ชอบ
- ติดตั้ง dependencies จาก `requirements.txt`

### 2. ไฟล์หลัก
- **main.py**: ใช้ `face_recognition` library สำหรับ face recognition
  - โหลดภาพจาก `known_people/yui.jpg`
  - เปรียบเทียบใบหน้าจากกล้องกับภาพที่รู้จัก
  - แสดงผลแบบ real-time พร้อมกรอบและชื่อ

- **app.py**: ใช้ `mediapipe` สำหรับ face detection
  - ตรวจจับใบหน้าจากกล้อง
  - แสดงกรอบใบหน้าที่ตรวจพบ

### 3. Dependencies หลัก
- `face-recognition==1.3.0` - สำหรับ face recognition
- `mediapipe==0.10.21` - สำหรับ face detection
- `opencv-python==4.11.0.86` - สำหรับการประมวลผลภาพ
- `dlib==20.0.0` - dependency ของ face_recognition

### 4. การใช้งาน
```bash
# สร้าง virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# หรือ venv\Scripts\activate  # Windows

# ติดตั้ง dependencies
pip install -r requirements.txt

# รัน Face Recognition
python main.py

# รัน Face Detection
python app.py
```

### 5. หมายเหตุสำคัญ
- กด ESC เพื่อออกจากโปรแกรม
- ภาพใน `known_people/` จะถูกใช้เป็น reference สำหรับ face recognition
- โปรเจคนี้ใช้กล้อง (camera index 0) เป็น input

### 6. การพัฒนาต่อ
- สามารถเพิ่มภาพใน `known_people/` เพื่อเพิ่มคนที่รู้จัก
- ปรับแต่ง confidence threshold ใน MediaPipe
- เพิ่มฟีเจอร์เช่น face landmarks, emotion detection

## สำหรับ AI ตัวถัดไป
โปรเจคนี้เป็นตัวอย่างการใช้งาน Computer Vision สำหรับ Face Recognition และ Face Detection โดยใช้ Python libraries ที่นิยม ควรระวังเรื่อง:
- การติดตั้ง dlib อาจมีปัญหาในบางระบบ
- ต้องมีกล้องที่ใช้งานได้
- ภาพใน known_people ควรมีคุณภาพดีและมีใบหน้าที่ชัดเจน # py_Mediapipe
