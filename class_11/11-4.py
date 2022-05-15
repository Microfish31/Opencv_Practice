import cv2
import numpy as np

img = cv2.imread('find_lines.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray,50,150)
lines = cv2.HoughLinesP(edges,1,np.pi/180,260,minLineLength=100,maxLineGap=50)

print(lines.shape)
print("L0=",lines[0])
print("L1=",lines[1])

for n in range(len(lines)) :
    x1 = lines[n,0,0]
    y1 = lines[n,0,1]
    x2 = lines[n,0,2]
    y2 = lines[n,0,3]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),5)
    cv2.imshow("img",img)
    cv2.waitKey()