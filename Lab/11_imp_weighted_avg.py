import numpy as np
import cv2
import matplotlib.pyplot as plt
def weighted_average_filter(image, kernel_size=3):
    # Ensure the kernel size is odd
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd number")
    
    # Create a kernel with weights (center pixel has the highest weight)
    weights = np.arange(1, kernel_size**2 + 1).reshape((kernel_size, kernel_size))
    kernel = weights / np.sum(weights)
    
    # Apply the filter to each channel (if the image is color)
    if len(image.shape) == 3:
        result = np.zeros_like(image, dtype=np.float32)
        for channel in range(image.shape[2]):
            result[:, :, channel] = cv2.filter2D(image[:, :, channel], -1, kernel)
    else:    
        result = cv2.filter2D(image, -1, kernel)
    
    return result.astype(np.uint8)

img = cv2.imread("./Lab/noisysalterpepper.png")
img = cv2.resize(img, (400, 300))
# Apply weighted average filtering with a 3x3 kernel
weighted_image = weighted_average_filter(img, kernel_size=3)

# Display the results
cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", weighted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()