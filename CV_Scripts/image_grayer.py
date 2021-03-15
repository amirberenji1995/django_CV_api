import cv2
from CV_Scripts.imageReader import imageReader
from CV_Scripts.imageWriter import imageWriter


def image_grayer(add, file):
    img = imageReader(add, file)
    grayed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    file_name = imageWriter(add, file, grayed_image)
    return 'processed_' + file_name
