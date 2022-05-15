import numpy as np
import cv2

# add cv2.CAP_DSHOW
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret1,img1 = cap.read()
ret2,img2 = cap.read()

while 1:

    diff = cv2.absdiff(img1,img2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(7,7),0)

    a,thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)

    get_white_area = np.where(thresh==255)

    X = int(np.average(get_white_area[1]))
    Y = int(np.average(get_white_area[0]))

    cv2.circle(img1,(X,Y),5,(255,0,0),3)

    cv2.imshow("img",img1)

    key = cv2.waitKey(100) & 0xFF

    # print(key)

    if key == ord("q"):
        print("break")
        break
    
    img1 = img2.copy()
    ret2,img2 = cap.read()

cap.release()
cv2.destroyAllWindows()