from flask import Flask, render_template, request
import face_recognition
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# โหลดใบหน้าที่รู้จัก
known_encodings = []
known_names = []

for filename in os.listdir('known_people'):
    if filename.endswith(('.jpg', '.png')):
        path = os.path.join('known_people', filename)
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)
        if encoding:
            known_encodings.append(encoding[0])
            known_names.append(os.path.splitext(filename)[0])

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # โหลดภาพและแปลงเป็น encoding
            image = face_recognition.load_image_file(filepath)
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                name = "Unknown"
                if True in matches:
                    index = matches.index(True)
                    name = known_names[index]
                names.append(name)

            message = f"พบใบหน้า: {', '.join(names)}"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
