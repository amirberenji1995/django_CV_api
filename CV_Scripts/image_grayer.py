import cv2


def image_grayer(add, file):
    file_name = file.split('/')[-1]
    img = cv2.imread(add + file)
    grayed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(add + '/media/' + 'processed_' + file_name, grayed_image)
    return 'processed_' + file_name
