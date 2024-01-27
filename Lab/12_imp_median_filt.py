import cv2
import numpy as np

# Read the image (adjust path if needed)
img = cv2.imread('./Lab/noisysalterpepper.png')
img_noisy1 = cv2.resize(img, (400, 300))
cv2.imshow('Original Image', img_noisy1)

# Get image dimensions (accounting for color channels)
m, n, _ = img_noisy1.shape  # Unpack height, width, and discard channels

# Create a new image array for the filtered result
img_new1 = np.zeros([m, n])

# Iterate through the image, applying median filtering
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = [
            img_noisy1[i - 1, j - 1],
            img_noisy1[i - 1, j],
            img_noisy1[i - 1, j + 1],
            img_noisy1[i, j - 1],
            img_noisy1[i, j],
            img_noisy1[i, j + 1],
            img_noisy1[i + 1, j - 1],
            img_noisy1[i + 1, j],
            img_noisy1[i + 1, j + 1]
        ]

        temp = np.sort(temp)
        img_new1[i, j] = temp[4][0]  # Assign the median value

# Convert to uint8 for display
img_new2 = img_new1.astype(np.uint8)

# Display the filtered image
cv2.imshow('Median Filtered Image', img_new2)
cv2.waitKey(0)
cv2.destroyAllWindows()