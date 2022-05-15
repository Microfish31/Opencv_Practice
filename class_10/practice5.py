# draw rectange contour
import cv2
import numpy as np

img = cv2.imread("google_contour.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thr",thr)

contours,a = cv2.findContours(thr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,0,255),thickness=2)

for c in contours:
    x0 = min(c[:,0,0]) 
    y0 = min(c[:,0,1])
    x1 = max(c[:,0,0])
    y1 = max(c[:,0,1])
    cv2.rectangle(img,(x0,y0),(x1,y1),(255,0,0),1)

# print(len(contours))
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()