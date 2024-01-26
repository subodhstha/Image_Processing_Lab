import cv2 
image = cv2.imread("./Lab/image.jpg")
image = cv2.resize(image, (400, 300))
cv2.imshow("Real image", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()