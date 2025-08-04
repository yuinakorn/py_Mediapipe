# Gitignore Configuration

## ไฟล์ .gitignore ที่สร้างขึ้น

### 1. วัตถุประสงค์
ไฟล์ `.gitignore` ถูกสร้างขึ้นเพื่อป้องกันไม่ให้ไฟล์ที่ไม่จำเป็นถูก commit เข้า Git repository

### 2. หมวดหมู่ไฟล์ที่ ignore

#### Python Standard
- `__pycache__/` - Python bytecode cache
- `*.pyc`, `*.pyo` - Compiled Python files
- `*.egg-info/` - Package metadata
- `build/`, `dist/` - Build directories

#### Virtual Environments
- `venv/`, `venv310/` - Python virtual environments
- `.env` - Environment variables
- `env/`, `.venv/` - Alternative virtual environment names

#### IDE/Editor Files
- `.idea/` - PyCharm settings
- `.vscode/` - VS Code settings
- `*.iml`, `*.ipr` - IntelliJ IDEA files

#### Operating System Files
- `.DS_Store` - macOS system files
- `Thumbs.db` - Windows thumbnail cache
- `*~` - Linux backup files

#### Project Specific
- `*.pkl`, `*.pickle` - Pickled model files
- `*.h5`, `*.hdf5` - HDF5 model files
- `*.mp4`, `*.avi` - Video files
- `*.jpg`, `*.png` - Image files (except known_people)
- `*.log` - Log files
- `temp/`, `tmp/` - Temporary directories

### 3. ไฟล์ที่ยังคงถูก track
- `known_people/` directory (แต่ ignore รูปภาพในนั้น)
- `requirements.txt`
- `main.py`, `app.py`
- `README.md` และไฟล์ .md อื่นๆ

### 4. การใช้งาน
```bash
# ตรวจสอบไฟล์ที่จะถูก ignore
git status --ignored

# เพิ่มไฟล์ที่ต้องการ ignore แบบเฉพาะเจาะจง
echo "specific_file.txt" >> .gitignore

# ตรวจสอบว่าไฟล์ถูก ignore หรือไม่
git check-ignore filename
```

### 5. หมายเหตุสำคัญ
- ไฟล์ `known_people/yui.jpg` จะยังคงถูก track เพราะเป็นไฟล์สำคัญของโปรเจค
- Virtual environment `venv310/` จะถูก ignore เพื่อไม่ให้ commit ไฟล์ขนาดใหญ่
- ไฟล์ log และ temporary จะถูก ignore เพื่อรักษาความสะอาดของ repository

## สำหรับ AI ตัวถัดไป
เมื่อเพิ่มไฟล์ใหม่:
1. ตรวจสอบว่าไฟล์ควรถูก ignore หรือไม่
2. อัปเดต .gitignore ถ้าจำเป็น
3. ระวังเรื่องไฟล์ที่มีข้อมูลส่วนตัวหรือ sensitive data
4. ตรวจสอบขนาดไฟล์ก่อน commit 