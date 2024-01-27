
import cv2

image = cv2.imread('../../images/NoisyButterFly.png')

# Gaussian blur
blurred_image = cv2.GaussianBlur(image, (25, 25), 0)

cv2.imwrite(
    "../../images/noise-removed-images/GaussianBlurOnColorImage.jpeg", blurred_image)
