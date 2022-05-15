# dilate
import numpy as np
import cv2

img = cv2.imread("img_dilate0422.jpg",0)

kernel = np.ones((10,10))

dilated = cv2.dilate(img,kernel,iterations=5)

cv2.imshow("o",img)
cv2.imshow("df",dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()