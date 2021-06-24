import cv2
from CV_Scripts.imageReader import imageReader
from CV_Scripts.imageWriter import imageWriter


def image_scaler(add, file, scale):
    img = imageReader(add, file)
    dst_width = int(img.shape[1] * scale / 100)
    dst_height = int(img.shape[0] * scale / 100)
    dsize = (dst_width, dst_height)
    resized = cv2.resize(img, dsize)
    file_name = imageWriter(add, file, resized)
    return 'processed_' + file_name
