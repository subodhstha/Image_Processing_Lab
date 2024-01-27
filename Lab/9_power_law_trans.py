import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./Lab/image.jpg')
gamma = 0.6
output = np.array(255 * (img / 255) ** gamma, dtype='uint8')

# cv2.imshow("Original Image", img)
# cv2.imshow("Gamma Corrected Image", s)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(output)
plt.title('Output Image')
plt.axis('off')
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()