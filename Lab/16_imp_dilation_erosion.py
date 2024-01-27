import cv2
import numpy as np

# Read the image (adjust path if needed)
img = cv2.imread('./Lab/Morphology.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (400, 500))

# Get image dimensions
m, n = img.shape

# Define the structuring element
se = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

# Initialize the output images
dilated_img = np.zeros([m, n], dtype=np.uint8)
eroded_img = np.ones([m, n], dtype=np.uint8) * 255

# Apply dilation
for i in range(1, m-1):
    for j in range(1, n-1):
        max_pixel = np.max(img[i-1:i+2, j-1:j+2])
        dilated_img[i, j] = max_pixel

# Apply erosion
for i in range(1, m-1):
    for j in range(1, n-1):
        min_pixel = np.min(img[i-1:i+2, j-1:j+2])
        eroded_img[i, j] = min_pixel

# Save the output images
out_image = np.hstack([img, dilated_img, eroded_img])
cv2.imshow('Original, Dilated and Eroded Image', out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
