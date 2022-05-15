# find the center of the coins 
import cv2
import numpy as np

cap = cv2.VideoCapture("coins.MOV")

while 1:
    ret,frame = cap.read()

    if ret :
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        ret,thr = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
        kernel = np.ones((5,5),np.uint8)
        kernel2 = np.ones((11,11),np.uint8)
        eroded = cv2.erode(thr,kernel,iterations=2)
        dilated = cv2.dilate(eroded,kernel2,iterations=3)
        contours,a = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,contours,-1,(0,255,0),thickness=5)
        for c in contours:
            x = int((max(c[:,0,0]) + min(c[:,0,0]))/2)
            y = int((max(c[:,0,1]) + min(c[:,0,1]))/2)
            cv2.circle(frame,(x,y),5,(255,0,0),-1)
        cv2.imshow("frame",frame)
        cv2.waitKey(10)
    else :
        break

cap.release()
cv2.destroyAllWindows()