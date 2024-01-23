
import cv2

image = cv2.imread('../../images/Goldfinch.jpg')

# Gaussian blur
blurred_image = cv2.GaussianBlur(image, (45, 45), 0)

cv2.imwrite("../../images/GaussianBlurOnColorImage.jpeg", blurred_image)
