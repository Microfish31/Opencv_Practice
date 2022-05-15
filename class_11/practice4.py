import cv2
import numpy as np

src = cv2.imread('euro.jpg')

gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,3)
edges = cv2.Canny(gray,180,250)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=250,param2=35,minRadius=20,maxRadius=100)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(src,(i[0],i[1]),i[2],(0,0,255),2)
    print('circle at:',i[0],i[1],'radius=',i[2])
    cv2.circle(src,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',src)
cv2.waitKey()
cv2.destroyAllWindows()