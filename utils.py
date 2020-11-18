from database import Database
import face_recognition

def getImg():
    db = Database()
    img = db.getAllImage()
    arr = []
    for i in img:
        arr.append("".join(i))

    return arr

def getNis():
    db = Database()
    nis = db.getNis()
    arr = []
    for j in nis:
        arr.append("".join(j))

    return arr

def encode():
    encoded = []
    known_face_nis = []
    count = 0

    for i in getImg():
        img = face_recognition.load_image_file(i)
        encoding = face_recognition.face_encodings(img)[0]
        encoded.append(encoding)
        count += 1
    for j in getNis():
        known_face_nis.append(j)

    return encoded, known_face_nis

