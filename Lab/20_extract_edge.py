import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('./Lab/image.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (400, 300))

# Apply the Canny edge detector
edges = cv2.Canny(image, 50, 150)

# Display the original and edge-detected images
# plt.subplot(121), plt.imshow(image, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Edge Extraction'), plt.xticks([]), plt.yticks([])
# plt.show()
out_image = np.hstack([image, edges])
cv2.imshow('Original and edge', out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()