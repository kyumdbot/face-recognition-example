import face_recognition
import cv2
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


def run(name):
    print("name: " + name)
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    new_name = name.replace(" ", "_");
    filename = 'images/' + new_name + '.jpg'

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('Take a photo',frame)
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
            cv2.imwrite(filename, frame)
            break

    cap.release()
    cv2.destroyAllWindows()

    print("\nWait...")
    user_image = face_recognition.load_image_file(filename)
    user_face_encoding = face_recognition.face_encodings(user_image)[0]
    print(user_face_encoding)

    json_str = numpy_to_json(user_face_encoding)
    add_to_db(name, json_str)


if len(sys.argv) <= 1:
    print("Please input a name!")
else:
    name = sys.argv[1] 
    run(name)

