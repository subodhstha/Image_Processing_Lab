import cv2
img= cv2.imread('./Lab/image.jpg')
img = cv2.resize(img, (400, 300))
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, bimage) = cv2.threshold(image, 100, 225, cv2.THRESH_BINARY)
cv2.imshow("Real image",img)
cv2.imshow("Back and white image",bimage)
cv2.waitKey(0)
cv2.destroyAllWindows()