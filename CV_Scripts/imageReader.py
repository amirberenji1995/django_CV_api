import cv2


def imageReader(add, file):
    img = cv2.imread(add + file)
    return img

