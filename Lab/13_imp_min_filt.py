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

# Iterate through the image, applying minimum filtering
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
        img_new1[i, j] = temp[3]  # Assign the minimum value

# Convert to uint8 for display
img_new2 = img_new1.astype(np.uint8)
both_image = np.hstack([img_noisy1, img_new2])

# Display the filtered image
cv2.imshow('original and Minimum Filtered Image', both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()