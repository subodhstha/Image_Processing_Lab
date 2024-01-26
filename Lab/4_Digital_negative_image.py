import cv2
img= cv2.imread('./Lab/image.jpg')
img = cv2.resize(img, (400, 300))
neg_img = cv2.bitwise_not(img)
cv2.imshow("Original Image", img)
cv2.imshow("Digital Negative Image", neg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()