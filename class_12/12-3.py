import cv2
from findMarker import findMaxContour as fm
import numpy as np

move_name = "motionPattens3.mov"
cap = cv2.VideoCapture(move_name)

while 1:
    ret,frame = cap.read()

    if ret :
        get_max_contour = fm(frame)
        rect = cv2.minAreaRect(get_max_contour)
        box = np.int64(cv2.boxPoints(rect))
        cv2.drawContours(frame,[box],0,(0,255,0),2)
        txt = 'width = ' + str(int(rect[1][0])) + ' pixel'
        cv2.putText(frame,txt,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.imshow("frame",frame)
        cv2.waitKey(10)
    else :
        break

cap.release()
cv2.destroyAllWindows()