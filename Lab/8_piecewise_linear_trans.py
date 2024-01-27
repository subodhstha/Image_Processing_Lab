import cv2
import numpy as np
import matplotlib.pyplot as plt

def piecewise_linear_transform(image, breakpoints, slopes):
    # Initialize the transformed image
    transformed_image = np.zeros_like(image)
    
    # Apply piecewise linear transformation
    for i in range(len(breakpoints) - 1):
        mask = np.logical_and(image >= breakpoints[i], image < breakpoints[i + 1])
        transformed_image = np.where(mask, slopes[i] * (image - breakpoints[i]), transformed_image)
    
    # Handle the last segment
    mask = image >= breakpoints[-1]
    transformed_image = np.where(mask, slopes[-1] * (image - breakpoints[-1]), transformed_image)
    
    return transformed_image.astype(np.uint8)

# Read an example image
original_image = cv2.imread('./Lab/image.jpg', cv2.IMREAD_GRAYSCALE)

# Define breakpoints and slopes for the piecewise linear transformation
breakpoints = [0, 100, 150, 255]
slopes = [0, 2, 0.5, 1]

# Apply piecewise linear transformation
transformed_image = piecewise_linear_transform(original_image, breakpoints, slopes)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(transformed_image, cmap='gray')
plt.title('Transformed Image')
plt.axis('off')

plt.show()