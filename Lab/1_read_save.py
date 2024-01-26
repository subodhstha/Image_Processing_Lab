import cv2
#Read the image
img = cv2.imread('./Lab/image.jpg')
img = cv2.resize(img, (400, 300))
#save the image
cv2.imwrite("Input Image.jpg", img)
#show the image
cv2.imshow("Output Image.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()