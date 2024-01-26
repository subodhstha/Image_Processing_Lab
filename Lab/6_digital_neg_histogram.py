import cv2
import matplotlib.pyplot as plt
 
 
# Read an image
img_bgr = cv2.imread('./Lab/image.jpg',3)
plt.imshow(img_bgr)
plt.title('Input Image')
plt.show()
 
# Histogram plotting of original image
color = ('b', 'g', 'r')
 
for i, col in enumerate(color):
     
    histr = cv2.calcHist([img_bgr],
                         [i], None,
                         [256],
                         [0, 256])
     
    plt.plot(histr, color = col)
     
    # Limit X - axis to 256
    plt.xlim([0, 256])
plt.title('Histogram of input Image')
plt.show()
 
# Negate the original image
img_neg = 1 - img_bgr

plt.imshow(img_neg)
plt.title('Output Image')
plt.show()
 
# Histogram plotting of
# negative transformed image
color = ('b', 'g', 'r')
 
for i, col in enumerate(color):
     
    histr = cv2.calcHist([img_neg],
                         [i], None,  
                         [256],
                         [0, 256])
     
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.title('Histogram of Output Image')     
plt.show()