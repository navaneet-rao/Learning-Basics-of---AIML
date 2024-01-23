import cv2

image_gray = cv2.imread('../../images/Goldfinch.jpg', cv2.IMREAD_GRAYSCALE)

image_blur = cv2.GaussianBlur(image_gray, (45,45), 0)

cv2.imwrite('../../images/OriginalGray.jpg', image_gray)
cv2.imwrite('../../images/Blurred.jpg', image_blur)
