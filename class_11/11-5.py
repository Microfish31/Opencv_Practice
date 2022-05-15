# problem
import cv2
import numpy as np

img = cv2.imread("Coin and Paper.jpg")
edges = cv2.Canny(img,150,200)

lines = cv2.HoughLines(edges,1,1*np.pi/100,60)

for n in range(lines.shape[0]-1):
    r = lines[n,0,0]
    q = lines[n,0,1]
    L = 1000
    x0 = int(r*np.cos(q))
    y0 = int(r*np.sin(q))
    x1 = int(x0+L*np.sin(q))
    y1 = int(y0-L*np.cos(q))
    x2 = int(x0-L*np.sin(q))
    y2 = int(y0+L*np.cos(q))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('img',img)

cv2.waitKey()
cv2.destroyAllWindows()
