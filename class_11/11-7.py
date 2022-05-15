# find the distance of the coins 
import cv2
import numpy as np

def distance(c1,c2) :
    delta_x = int(c1[0])-int(c2[0])
    delta_y = int(c1[1])-int(c2[1])
    return int( np.sqrt(delta_x**2+delta_y**2) )

cap = cv2.VideoCapture("2coins_motion.wmv")

while 1:
    ret,frame = cap.read()

    if ret :
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,3)

        edges = cv2.Canny(gray,20,200)
        # cv2.imshow('safsa',edges)
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70,param1=180,param2=25,minRadius=5,maxRadius=100)
        circles = np.uint16(np.around(circles))
        c1 = circles[0,0]
        c2 = circles[0,1]
        d = distance(c1,c2)

        cv2.circle(frame,(c1[0],c1[1]),c1[2],(0,0,255),2)
        cv2.circle(frame,(c2[0],c2[1]),c2[2],(0,0,255),2)
        cv2.line(frame,(c1[0],c1[1]),(c2[0],c2[1]),(0,255,0),3)
        txt = "D=" + str(np.round(d,2))
        cv2.putText(frame,txt,(30,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,5),1,cv2.LINE_AA)
        cv2.imshow('result',frame)
        cv2.waitKey(10)
    else :
        break

cap.release()
cv2.destroyAllWindows()
