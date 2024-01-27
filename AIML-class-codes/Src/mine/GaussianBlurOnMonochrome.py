import cv2
image = cv2.imread('../../images/NoisyButterFly.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = 120
_, binary_image = cv2.threshold(
    gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Invert the binary image to have white background
binary_image = cv2.bitwise_not(binary_image)

image_blur = cv2.GaussianBlur(binary_image, (45, 45), 0)

cv2.imwrite("../../images/binary.jpeg", binary_image)
cv2.imwrite('../../images/MonochromeBlurred.jpg', image_blur)
