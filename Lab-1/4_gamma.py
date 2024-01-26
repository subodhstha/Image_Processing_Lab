import cv2
import numpy as np
image= cv2.imread('./Lab-1/projects.jpg')
image= cv2.resize(image,(400, 500))
cv2.imshow('Original',image)
gamma=0.2
gamma_corrected = np.array(255*(image / 255) ** gamma, dtype = 'uint8')
cv2.imshow('Gamma Corrected',gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()