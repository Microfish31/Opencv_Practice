# draw rectange contour
import cv2
import random

img = cv2.imread("google_contour.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thr",thr)

contours,a = cv2.findContours(thr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    # cv2.circle(img,(x+w,y),2,(255,0,0,),2)
    print((x+w,y))
    b,g,r = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    cv2.rectangle(img,(x,y),(x+w,y+h),(b,g,r),3)
    cv2.imshow("img",img)
    cv2.waitKey(500)

cv2.destroyAllWindows()