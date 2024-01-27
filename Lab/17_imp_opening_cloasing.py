import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('./Lab/ope.webp', 0)

# Create a rectangular kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Opening operation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing operation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display the original, opening, and closing images
# cv2.imshow('Original Image', img)
# cv2.imshow('Opening Result', opening)
# cv2.imshow('Closing Result', closing)
out_image = np.hstack([img, opening, closing])
cv2.imshow('Original, Dilated and Eroded Image', out_image)

cv2.waitKey(0)
cv2.destroyAllWindows()