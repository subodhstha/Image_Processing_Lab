import cv2

img= cv2.imread('./Lab-1/projects.jpg')
# img = cv2.resize(img, (800, 600))
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, bimage) = cv2.threshold(image, 200, 225, cv2.THRESH_BINARY)
cv2.imshow("Real image",img)
cv2.imshow("image",bimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
