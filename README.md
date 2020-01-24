## Setup

1. Install numpy:

```
$ pip3 install numpy
```

2. Compile and Install dlib:

```
$ mkdir temp; cd temp
$ git clone https://github.com/davisking/dlib.git
$ cd dlib
$ mkdir build; cd build
$ cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
$ cmake --build .
$ cd ..
$ python3 setup.py install
$ sudo ldconfig
$ cd ~
```

3. Install face_recognition:

```
$ pip3 install face_recognition
```

4. Clone this repo:

```
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

 ( Press 'y' key to take a photo and register. )

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

