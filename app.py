import face_recognition
from flask import Flask, jsonify, request, redirect
from database import Database
import numpy as np
from utils import getImg, getNis, encode
import sys

addr = sys.argv[1]

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            return detect_faces(file)

    return '''
    <!doctype html>
    <h1>Upload</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


def detect_faces(file_stream):
    known_face = encode()[0]
    known_face_nis = encode()[1]
    print(known_face_nis)

    img = face_recognition.load_image_file(file_stream)
    face_encodings = face_recognition.face_encodings(img)

    face_found = False

    nis = "Unkown"

    for unknown_face_encodings in face_encodings:


        if len(unknown_face_encodings) > 0:
            face_found = True

        matches = face_recognition.compare_faces(known_face, unknown_face_encodings)
        face_distances = face_recognition.face_distance(known_face, unknown_face_encodings)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            nis = known_face_nis[best_match_index]
   
    result = {
        "wajah_ditemukan": face_found,
        "NIS": nis
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host=addr, port=5001, debug=True)
