import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./Lab/image.jpg')
# cv2.imshow('input image', img)

c = (255 / np.log(1 + np.max(img)))
log_trx_img = c * np.log(1 + img)
log_trx_img = np.array(log_trx_img, dtype='uint8')

# cv2.imshow('log transform image', log_trx_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(log_trx_img)
plt.title('log transform  image')
plt.axis('off')
plt.show()