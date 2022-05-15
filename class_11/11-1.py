import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("0518_5p.png",0)
flag,thresh = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
# cv2.imshow('sad',thresh)
# th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,7,1)
# kernel = np.ones((2,2),np.uint8)
# eroded = cv2.erode(th,kernel,iterations=1)
# dilated = cv2.dilate(eroded,kernel,iterations=3)
edge = cv2.Canny(thresh,200,250)

# cv2.imshow("img",img)
# cv2.imshow("th",th)
# cv2.imshow("eroded",eroded)
# cv2.imshow("dilated",dilated)
# cv2.imshow("edge",edge)
pos = np.where(edge==255)

cv2.waitKey(0)
cv2.destroyAllWindows()
x = pos[0]
y = pos[1]
# print(x)
# print(y)
# x = x[120:]
# y = y[120:]
plt.plot(x,y,'o')
plt.imshow(edge)
plt.show()