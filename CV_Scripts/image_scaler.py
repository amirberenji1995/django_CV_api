import cv2
from CV_Scripts.imageReader import imageReader
from CV_Scripts.imageWriter import imageWriter


def image_scaler(add, file, scale_percent):
    img = imageReader(add, file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dst_width = int(img.shape[1] * scale_percent / 100)
    dst_heigth = int(img.shape[0] * scale_percent / 100)
    dsize = (dst_width, dst_heigth)
    resized = cv2.resize(img, dsize)
    file_name = imageWriter(add, file, resized)
    return 'processed_' + file_name
