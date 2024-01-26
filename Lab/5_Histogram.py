import cv2
import matplotlib.pyplot as plt
img= cv2.imread('./Lab/image.jpg')
img = cv2.resize(img, (400, 300))
cv2.imshow('input',img)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()