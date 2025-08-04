# Web Interface Guide

## ภาพรวม

Web Interface ของโปรเจคนี้สร้างด้วย Flask และใช้ MediaPipe สำหรับ Liveness Detection โดยมีฟีเจอร์หลักคือการตรวจจับการกระพริบตาและยิ้มเพื่อยืนยันว่าเป็นบุคคลจริง

## ฟีเจอร์หลัก

### 1. Liveness Detection
- **การตรวจจับการกระพริบตา** - ใช้ MediaPipe Face Mesh
- **การตรวจจับการยิ้ม** - วัดระยะห่างของปาก
- **Real-time Processing** - ประมวลผลแบบ real-time

### 2. Web Interface
- **Responsive Design** - รองรับทุกขนาดหน้าจอ
- **Thai Language Support** - แสดงข้อความภาษาไทยได้ถูกต้อง
- **Real-time Status Updates** - อัปเดตสถานะแบบ real-time
- **Modern UI** - ออกแบบสวยงามและใช้งานง่าย

### 3. Technical Features
- **Server-Sent Events** - สำหรับ real-time communication
- **CORS Support** - รองรับการเข้าถึงจากทุก domain
- **Error Handling** - จัดการข้อผิดพลาดอย่างเหมาะสม

## การติดตั้งและใช้งาน

### 1. การติดตั้ง Dependencies
```bash
# เปิด virtual environment
source venv310/bin/activate

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### 2. การรันเซิร์ฟเวอร์
```bash
# รัน web server
python app.py
```

### 3. การเข้าถึง
- **URL หลัก**: http://localhost:8080
- **URL สำรอง**: http://127.0.0.1:8080
- **Test Endpoint**: http://localhost:8080/test

## โครงสร้างไฟล์

### ไฟล์หลัก
- `app.py` - Flask application หลัก
- `templates/index.html` - Web interface template

### Dependencies ที่ใช้
```txt
Flask==3.1.1
flask-cors==4.0.0
mediapipe==0.10.21
opencv-python==4.12.0.88
numpy==2.2.6
```

## API Endpoints

### 1. `/` (GET)
- **หน้าที่**: แสดงหน้าเว็บหลัก
- **Response**: HTML template

### 2. `/video_feed` (GET)
- **หน้าที่**: ส่งวิดีโอสตรีมจากกล้อง
- **Response**: Multipart video stream
- **Content-Type**: `multipart/x-mixed-replace; boundary=frame`

### 3. `/status_feed` (GET)
- **หน้าที่**: ส่งข้อมูลสถานะแบบ real-time
- **Response**: Server-Sent Events stream
- **Content-Type**: `text/event-stream`

### 4. `/test` (GET)
- **หน้าที่**: ทดสอบการทำงานของเซิร์ฟเวอร์
- **Response**: JSON
```json
{
  "status": "OK",
  "message": "Server is running"
}
```

## ข้อมูลสถานะ (Status Data)

### โครงสร้างข้อมูล
```json
{
  "message_key": "waiting",
  "message_th": "โปรดกระพริบตาหรือยิ้ม...",
  "message_en": "Please blink or smile...",
  "has_face": 1,
  "is_blinking": 0,
  "is_smiling": 0
}
```

### ประเภทสถานะ
1. **no_face** - ไม่พบใบหน้า
2. **waiting** - รอการกระพริบตาหรือยิ้ม
3. **blinking** - ตรวจพบการกระพริบตา
4. **smiling** - ตรวจพบการยิ้ม

## การแก้ไขปัญหา

### 1. ปัญหา Port 5000 ถูกใช้งาน
**สาเหตุ**: AirPlay Receiver บน macOS ใช้ port 5000
**การแก้ไข**: เปลี่ยนเป็น port 8080

### 2. ปัญหาการแสดงผลภาษาไทย
**สาเหตุ**: OpenCV ไม่รองรับฟอนต์ภาษาไทย
**การแก้ไข**: ย้ายข้อความไปแสดงใน HTML

### 3. ปัญหา JSON Serialization
**สาเหตุ**: Boolean values ไม่สามารถ serialize เป็น JSON ได้
**การแก้ไข**: เปลี่ยน boolean เป็น integer (0/1)

### 4. ปัญหาการเชื่อมต่อถูกตัด
**สาเหตุ**: CORS หรือการตั้งค่าเซิร์ฟเวอร์
**การแก้ไข**: เพิ่ม CORS support และปรับการตั้งค่า

## การปรับแต่ง

### 1. เปลี่ยน Port
แก้ไขใน `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
```

### 2. ปรับเกณฑ์ Liveness Detection
แก้ไขใน `app.py`:
```python
# เกณฑ์การกระพริบตา
is_blinking = left_eye_open < 0.01 and right_eye_open < 0.01

# เกณฑ์การยิ้ม
is_smiling = mouth_width > 0.08
```

### 3. ปรับแต่ง UI
แก้ไขใน `templates/index.html`:
- เปลี่ยนสีและสไตล์ใน CSS
- เพิ่ม/ลบฟีเจอร์ใน JavaScript
- ปรับข้อความใน HTML

## การพัฒนาเพิ่มเติม

### ฟีเจอร์ที่แนะนำ
- [ ] การบันทึกผลการตรวจสอบ
- [ ] การส่งแจ้งเตือน
- [ ] การปรับแต่งเกณฑ์แบบ real-time
- [ ] การเพิ่ม/ลบคนในระบบ
- [ ] การแสดงสถิติการใช้งาน

### การปรับปรุงประสิทธิภาพ
- [ ] การใช้ WebRTC แทน video stream
- [ ] การประมวลผลแบบ WebAssembly
- [ ] การใช้ Web Workers
- [ ] การเพิ่ม caching

## หมายเหตุสำคัญ

1. **กล้อง**: ต้องมีกล้องที่ใช้งานได้
2. **Browser**: รองรับ Server-Sent Events
3. **Network**: ต้องมีการเชื่อมต่อที่เสถียร
4. **Performance**: อาจใช้ CPU สูงขึ้นเมื่อประมวลผล

## การทดสอบ

### 1. ทดสอบการเชื่อมต่อ
```bash
curl http://localhost:8080/test
```

### 2. ทดสอบ Video Feed
เปิด http://localhost:8080/video_feed ในเบราว์เซอร์

### 3. ทดสอบ Status Feed
```bash
curl -N http://localhost:8080/status_feed
```

## สรุป

Web Interface นี้ให้ประสบการณ์การใช้งานที่ดีสำหรับ Liveness Detection โดยมีฟีเจอร์ที่ครบครันและใช้งานง่าย เหมาะสำหรับการใช้งานจริงและการพัฒนาต่อ 