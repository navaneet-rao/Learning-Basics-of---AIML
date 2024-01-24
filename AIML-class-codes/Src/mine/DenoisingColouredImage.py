import cv2

img = cv2.imread('../../images/ButterFly.png')

dst = cv2.fastNlMeansDenoisingColored(img, None, 25, 25, 7, 15)


cv2.imwrite('../../images/NewButterFly.png', dst)