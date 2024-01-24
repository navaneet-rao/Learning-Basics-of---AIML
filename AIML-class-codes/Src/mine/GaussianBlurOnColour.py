import cv2
import numpy as np

# Load the image
image = cv2.imread('../../images/Goldfinch.jpg')

# Convert the image to float32
image = image.astype(np.float32)

# Specify the mean and standard deviation for the Gaussian noise
mean = 0   
stddev = 100 # This value can be changed to increase/decrease the noise level in the image

# Generate Gaussian noise
noise = np.random.normal(mean, stddev, image.shape)

# Add the noise to the image
noisy_image = image + noise

# Clip the values to be within the valid image pixel range [0, 255]
noisy_image = np.clip(noisy_image, 0, 255)

# Convert the image back to uint8
noisy_image = noisy_image.astype(np.uint8)

cv2.imwrite('../../images/NoisyButterFly.png', noisy_image)
