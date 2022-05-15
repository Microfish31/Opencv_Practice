import numpy as np
import cv2

img = cv2.imread("circles.jpg",0)

kernel = np.ones((7,7),np.uint8)

eroded = cv2.erode(img,kernel,iterations=2)

cv2.imshow("img",img)
cv2.imshow("eroded",eroded)

kernel2 = np.ones((7,7),np.uint8)

dilated = cv2.dilate(eroded,kernel2,iterations=2)

cv2.imshow("dilated",dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()