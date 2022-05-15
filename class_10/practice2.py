# erode
import numpy as np
import cv2

img = cv2.imread("img_dilate0422.jpg",0)

kernel = np.ones((3,3),np.uint8)

eroded = cv2.erode(img,kernel,iterations=2)

cv2.imshow("o",img)
cv2.imshow("erd",eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()