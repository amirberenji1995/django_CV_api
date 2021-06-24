import cv2
from CV_Scripts.imageReader import imageReader
from CV_Scripts.imageWriter import imageWriter


def imageResizer(add, file, width, height):
    img = imageReader(add, file)
    resized = cv2.resize(img, (width, height))
    file_name = imageWriter(add, file, resized)
    return 'processed_' + file_name