 # Git Setup and Usage Guide

## การเริ่มใช้ Git ในโปรเจค

### 1. การเริ่มต้น Git Repository
```bash
# เริ่มต้น Git repository
git init

# ตรวจสอบสถานะ
git status

# เพิ่มไฟล์ทั้งหมดเข้า staging area
git add .

# Commit ครั้งแรก
git commit -m "Initial commit: Python Face Recognition project with MediaPipe"
```

### 2. ไฟล์ที่ถูก commit ในครั้งแรก
- `.gitignore` - Git ignore rules
- `README.md` - โปรเจค documentation
- `main.py` - Face recognition ด้วย face_recognition library
- `app.py` - Face detection ด้วย MediaPipe
- `requirements.txt` - Python dependencies
- `face_recognition_updates.md` - บันทึกการอัปเดต
- `gitignore_info.md` - ข้อมูล .gitignore
- `python_path_info.md` - ข้อมูล Python paths

### 3. Commit History
```
af98428 (HEAD -> main) Initial commit: Python Face Recognition project with MediaPipe
```

### 4. คำสั่ง Git พื้นฐาน

#### การตรวจสอบสถานะ
```bash
# ดูสถานะปัจจุบัน
git status

# ดู commit history
git log --oneline

# ดูการเปลี่ยนแปลงในไฟล์
git diff
```

#### การเพิ่มและ Commit
```bash
# เพิ่มไฟล์เฉพาะ
git add filename.py

# เพิ่มไฟล์ทั้งหมด
git add .

# Commit พร้อมข้อความ
git commit -m "Description of changes"

# Commit แบบ interactive
git commit
```

#### การดูประวัติ
```bash
# ดู commit history แบบย่อ
git log --oneline

# ดู commit history แบบละเอียด
git log

# ดูการเปลี่ยนแปลงใน commit
git show <commit-hash>
```

### 5. การทำงานกับ Remote Repository (ถ้ามี)
```bash
# เพิ่ม remote repository
git remote add origin <repository-url>

# Push ไปยัง remote
git push -u origin main

# Pull จาก remote
git pull origin main

# Clone repository
git clone <repository-url>
```

### 6. การจัดการ Branch
```bash
# สร้าง branch ใหม่
git branch feature-name

# เปลี่ยนไปยัง branch
git checkout feature-name

# สร้างและเปลี่ยน branch ในคำสั่งเดียว
git checkout -b feature-name

# ดู branch ทั้งหมด
git branch

# Merge branch
git merge feature-name
```

### 7. การ Undo และ Reset
```bash
# ยกเลิกการเปลี่ยนแปลงในไฟล์
git checkout -- filename.py

# ยกเลิกการ add
git reset HEAD filename.py

# ยกเลิก commit ล่าสุด
git reset --soft HEAD~1

# ยกเลิก commit และการเปลี่ยนแปลง
git reset --hard HEAD~1
```

### 8. หมายเหตุสำคัญ
- ใช้ commit message ที่อธิบายการเปลี่ยนแปลงอย่างชัดเจน
- Commit บ่อยๆ เพื่อรักษาประวัติการทำงาน
- ใช้ .gitignore เพื่อไม่ให้ commit ไฟล์ที่ไม่จำเป็น
- ตรวจสอบ git status ก่อน commit เสมอ

## สำหรับ AI ตัวถัดไป
เมื่อทำงานกับ Git:
1. ตรวจสอบ git status ก่อนทำการเปลี่ยนแปลง
2. ใช้ commit message ที่อธิบายการเปลี่ยนแปลง
3. อัปเดตไฟล์ .md เมื่อมีการเปลี่ยนแปลงสำคัญ
4. ใช้ branch สำหรับฟีเจอร์ใหม่
5. ตรวจสอบ .gitignore ว่าครอบคลุมไฟล์ที่ควร ignore