import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./images/Goldfinch.jpg')

# Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite("./images/GaussianBlurOnColorImage.jpeg", blurred_image)
