import face_recognition
import numpy as np
import sys
import json
import sqlite3


def numpy_to_json(n_array):
    n_list = n_array.tolist()
    j_array = json.dumps(n_list) 
    return j_array
    
def json_to_numpy(j_data):
    j_array = json.loads(j_data)
    n_array = numpy.array(j_array)
    return n_array

def add_to_db(name, json_str):
    conn = sqlite3.connect('facedb.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Members WHERE username = ?", (name,))
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute('INSERT INTO Members (username,faceencode) VALUES (?,?)', (name,json_str))
        conn.commit()
    else:
        print("Name already exists!")
    conn.close()
    print("ok")


def run(name, image_path):
    print("name: " + name)
    print("face image: " + image_path)
    print("\nWait...")
    user_image = face_recognition.load_image_file(image_path)
    user_face_encoding = face_recognition.face_encodings(user_image)[0]
    print(user_face_encoding)

    json_str = numpy_to_json(user_face_encoding)
    add_to_db(name, json_str)


if len(sys.argv) >= 3:
    name = sys.argv[1]
    image_path = sys.argv[2]
    run(name, image_path)
else:
    print('command: register_face.py "User Name" "FaceImageFilePath"')

