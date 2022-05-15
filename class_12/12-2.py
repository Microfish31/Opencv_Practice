import cv2
from findMarker import findMarkerByImg as fm

move_name = "motionPattens2.mov"
cap = cv2.VideoCapture(move_name)

while 1:
    ret,frame = cap.read()

    if ret :
        get = fm(frame)
        cv2.imshow("get",get)
        cv2.waitKey(10)
    else :
        break

cap.release()
cv2.destroyAllWindows()