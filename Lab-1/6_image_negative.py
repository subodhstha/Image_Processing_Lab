# image negative

import cv2 
import matplotlib as plt

img = cv2.imread('./Lab-1/grayscale.png')

cv2.imshow('Input Image', img)

img_neg = 255 - img

cv2.imshow('Output Image', img_neg)
cv2.waitKey(0)

cv2.destroyAllWindows()