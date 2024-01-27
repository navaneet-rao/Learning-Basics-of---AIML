import cv2

image_gray = cv2.imread('../../images/NoisyButterFly.png', cv2.IMREAD_GRAYSCALE)

image_blur = cv2.GaussianBlur(image_gray, (15,15), 0)

cv2.imwrite('../../images/OriginalGray.jpg', image_gray)
cv2.imwrite('../../images/GrayBlurred.jpg', image_blur)
