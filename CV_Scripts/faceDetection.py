import cv2
from CV_Scripts.imageReader import imageReader
from CV_Scripts.imageWriter import imageWriter


def face_detector(add, file):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = imageReader(add, file)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    file_name = imageWriter(add, file, img)
    return 'processed_' + file_name
