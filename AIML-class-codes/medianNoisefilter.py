import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('Source/noisy3.png')  # Replace 'your_image_path.jpg' with the path to your image file

# Apply Gaussian blur to the image
blurred_image = cv2.medianBlur(image, 5)

cv2.imwrite("./Result/noisy3-median.png",blurred_image)
