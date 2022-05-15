# To find moving object and square it.
import cv2
import numpy as np

cap = cv2.VideoCapture("viewFromME_video1.mp4")
ret,frame1 = cap.read()

while 1:
    ret2,frame2 = cap.read()

    if ret :
        diff = cv2.absdiff(frame1,frame2)
        diff = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

        ret,thr = cv2.threshold(diff,150,250,cv2.THRESH_BINARY)
        cv2.imshow("thr",thr)

        kernel = np.ones((1,1),np.uint8)
        eroded = cv2.erode(thr,kernel,iterations=2)

        kernel2 = np.ones((3,3),np.uint8)
        dilated = cv2.dilate(eroded,kernel2,iterations=11)

        cv2.imshow("dilated",dilated)

        contours,a = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            L = cv2.arcLength(c,True)
            if L > 100:
                cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("frame1",frame1)

        cv2.waitKey(10)
        
        frame1 = frame2.copy()

        ret2,frame2 = cap.read()

        if not ret2 :
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()