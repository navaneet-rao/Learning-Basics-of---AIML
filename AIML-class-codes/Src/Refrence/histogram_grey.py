import cv2
import matplotlib.pyplot as plt

# Load the color image
image = cv2.imread('Source/noisy2.jpeg')
# print(image.shape)
# print(image.size)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imwrite("./Result/noisy2-grey.jpeg",gray_image)

# Plot the histogram for the grayscale image
plt.hist(gray_image.ravel(), bins=256, color='black', alpha=0.7, rwidth=0.8)
plt.title('Grayscale Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
