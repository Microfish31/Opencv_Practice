import cv2
import numpy as np

src = cv2.imread('severalPatten.jpg')

gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,3)

edges = cv2.Canny(gray,20,200)
cv2.imshow('safsa',edges)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70,param1=180,param2=25,minRadius=5,maxRadius=100)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(src,(i[0],i[1]),i[2],(0,0,255),2)
    print('circle at:',i[0],i[1],'radius=',i[2])
    cv2.circle(src,(i[0],i[1]),2,(0,0,255),3)
    txt = "A:" + str(np.round(i[2]*i[2]*np.pi,2))
    cv2.putText(src,txt,(i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,5),1,cv2.LINE_AA)


cv2.imshow('detected circles',src)
cv2.waitKey()
cv2.destroyAllWindows()