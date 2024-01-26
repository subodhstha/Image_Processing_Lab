import cv2
import numpy as np
img= cv2.imread('./Lab-1/projects.jpg')
cv2.imshow('Original',img)
c=(255/np.log(1+np.max(img)))
log_transformed = c * (np.log(img + 1))
log_transformed = np.array(log_transformed, dtype = np.uint8)
cv2.imshow('Log Transformed',log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()