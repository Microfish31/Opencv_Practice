# Contour

import cv2

cap = cv2.VideoCapture(0)

ret,frame = cap.read()
cap.release()

if ret :
    cv2.imshow('frame',frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
