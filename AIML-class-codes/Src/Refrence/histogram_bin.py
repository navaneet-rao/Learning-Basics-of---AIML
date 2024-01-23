import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the color image
image = cv2.imread('Source/noisy2.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set a threshold to create a binary image
threshold_value = 200  # Adjust this value based on your image
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Invert the binary image to have white background
binary_image = cv2.bitwise_not(binary_image)

cv2.imwrite("./Result/noisy-bin.jpeg",binary_image)

# Plot the histogram for the grayscale image
plt.hist(binary_image.ravel(), bins=256, color='black', alpha=0.7, rwidth=0.8)
plt.title('Binary Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
