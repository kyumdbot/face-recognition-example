## Setup

```
$ pip3 install numpy
$ pip3 install dlib
$ pip3 install face_recognition
$ git clone https://github.com/kyumdbot/face-recognition-example.git
$ cd face-recognition-example
$ mkdir images
```

## Usage

1. Create database:

```
$ python3 create_database.py
```

2. Register your face:

```
$ python3 take_a_face.py "Your Name"
```

 ( Press 'y' key to take a photo. )

<br>

Or using picture file:

```
$ python3 register_face.py "Yuor Name" images/your_face.jpg
```


3. Face recognition

```
$ python3 face_recognition_camera.py
```

 ( Press 'q' key to quit. )

