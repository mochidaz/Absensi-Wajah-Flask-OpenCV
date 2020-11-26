from datetime import datetime as dt
import requests
from database import Database
import sys

db = Database()
file = sys.argv[1]

url = "http://0.0.0.0:5001"
files = {"file":open(file, 'rb')}

# POST request
r = requests.post(url, files=files).json()

print(r)

q = db.getAll(r['NIS'])
arr = []
count = 0
for i in q[0]:
    arr.append(i)
print("Data diri: ", arr)

nama = arr[0]
kelas = arr[1]
umur = arr[2]
nis = arr[3]
foto = arr[4]
timestamp = dt.now()

# Insert ke database Kehadiran
db.Kehadiran((nama, nis, kelas, foto, timestamp))


