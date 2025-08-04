# Project Structure and Documentation

## โครงสร้างโปรเจคปัจจุบัน

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
    ├── project_structure.md      # ไฟล์นี้
    ├── python_path_info.md       # ข้อมูล Python paths
    ├── face_recognition_updates.md # การอัปเดต face recognition
    ├── gitignore_info.md         # ข้อมูล .gitignore
    └── git_setup_info.md         # การตั้งค่า Git
```

## การย้ายไฟล์เอกสาร

### วันที่: 4 สิงหาคม 2025

**การเปลี่ยนแปลง:**
- สร้างโฟลเดอร์ `docs/` สำหรับเก็บเอกสาร
- ย้ายไฟล์ .md ที่ไม่ใช่ README.md ไปยังโฟลเดอร์ `docs/`
- `README.md` ยังคงอยู่ที่ root directory

**ไฟล์ที่ย้าย:**
- `face_recognition_updates.md` → `docs/face_recognition_updates.md`
- `gitignore_info.md` → `docs/gitignore_info.md`
- `python_path_info.md` → `docs/python_path_info.md`
- `git_setup_info.md` → `docs/git_setup_info.md`

**ไฟล์ที่ยังคงอยู่ที่ root:**
- `README.md` - เอกสารหลักของโปรเจค

## วัตถุประสงค์ของโครงสร้างใหม่

### 1. ความเป็นระเบียบ
- แยกเอกสารออกจากไฟล์โค้ดหลัก
- ง่ายต่อการค้นหาและจัดการเอกสาร
- โครงสร้างโปรเจคที่ชัดเจน

### 2. การบำรุงรักษา
- เอกสารทั้งหมดอยู่ในที่เดียว
- ง่ายต่อการอัปเดตและแก้ไข
- ไม่รบกวนไฟล์โค้ดหลัก

### 3. การทำงานเป็นทีม
- AI ตัวถัดไปจะรู้ว่าต้องเขียนไฟล์ .md ใน `docs/`
- เอกสารมีโครงสร้างที่ชัดเจน
- ง่ายต่อการติดตามการเปลี่ยนแปลง

## คำสั่งที่ใช้

```bash
# สร้างโฟลเดอร์ docs
mkdir docs

# ย้ายไฟล์ .md ไปยัง docs/
mv face_recognition_updates.md gitignore_info.md python_path_info.md git_setup_info.md docs/

# ตรวจสอบโครงสร้าง
ls -la
ls -la docs/
```

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