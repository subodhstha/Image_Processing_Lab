import cv2
img = cv2.imread("./Lab-1/projects.jpg")
cv2.imshow("original",img)
img_not = cv2.bitwise_not(img)
cv2.imshow("inverted",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
