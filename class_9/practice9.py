import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret1,img1 = cap.read()
ret2,img2 = cap.read()

for i in range(0,200) :

    diff = cv2.absdiff(img1,img2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(7,7),0)

    a,thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)

    get_white_area = np.where(thresh==255)

    X = int(np.average(get_white_area[1]))
    Y = int(np.average(get_white_area[0]))

    cv2.circle(img1,(X,Y),5,(255,0,0),3)
    cv2.imshow("img",img1)
    img1 = img2.copy()
    cv2.waitKey(100)
    ret2,img2 = cap.read()
    print(i)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()