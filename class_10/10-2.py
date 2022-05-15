import cv2
import numpy as np

img = cv2.imread("google_contour.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thr",thr)

kernel = np.ones((5,5),np.uint8)
dilated = cv2.dilate(thr,kernel,iterations=3)

cv2.imshow("dilated",dilated)

contours,a = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),thickness=2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
