import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('Source/noisy2.jpeg')  # Replace 'your_image_path.jpg' with the path to your image file

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite("./Result/noisy2-mean.jpeg",blurred_image)
