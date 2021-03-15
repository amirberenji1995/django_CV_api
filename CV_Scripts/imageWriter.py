import cv2


def imageWriter(add, file, img):
    file_name = file.split('/')[-1]
    cv2.imwrite(add + '/media/' + 'processed_' + file_name, img)
    return file_name
