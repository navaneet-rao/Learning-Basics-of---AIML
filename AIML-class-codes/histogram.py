import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Source/noisy2.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(4, 4))

# Blue channel histogram
plt.hist(image_rgb[:, :, 0].ravel(), bins=256, color='blue', alpha=0.7, rwidth=0.8)
plt.hist(image_rgb[:, :, 1].ravel(), bins=256, color='green', alpha=0.7, rwidth=0.8)
plt.hist(image_rgb[:, :, 2].ravel(), bins=256, color='red', alpha=0.7, rwidth=0.8)

plt.show()


# plt.figure(figsize=(4, 4))

# plt.show()

# plt.figure(figsize=(4, 4))

# plt.show()