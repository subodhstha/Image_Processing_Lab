import cv2
import numpy as np

# Read the image (adjust path if needed)
img = cv2.imread('./Lab/noisysalterpepper.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_noisy1 = cv2.resize(img, (400, 300))

# Get image dimensions (accounting for color channels)
m, n = img_noisy1.shape  # Unpack height, width, and discard channels

# Create a new image array for the filtered result
img_new1 = np.zeros([m, n])

# Create a Gaussian kernel
gaussian_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

# Iterate through the image, applying Gaussian blurring
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = [
            img_noisy1[i - 1, j - 1] * gaussian_kernel[0, 0],
            img_noisy1[i - 1, j] * gaussian_kernel[0, 1],
            img_noisy1[i - 1, j + 1] * gaussian_kernel[0, 2],
            img_noisy1[i, j - 1] * gaussian_kernel[1, 0],
            img_noisy1[i, j] * gaussian_kernel[1, 1],
            img_noisy1[i, j + 1] * gaussian_kernel[1, 2],
            img_noisy1[i + 1, j - 1] * gaussian_kernel[2, 0],
            img_noisy1[i + 1, j] * gaussian_kernel[2, 1],
            img_noisy1[i + 1, j + 1] * gaussian_kernel[2, 2]
        ]

        img_new1[i, j] = sum(temp)  # Assign the blurred value

# Convert to uint8 for display
img_new2 = img_new1.astype(np.uint8)
both_image = np.hstack([img_noisy1, img_new2])

# Display the filtered image
cv2.imshow('original and Gaussian Blurred Image', both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()