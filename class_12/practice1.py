import cv2

img = cv2.imread("A4paper70cm.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

a,thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)

contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cnt_max = max(contours,key=cv2.contourArea)

cv2.drawContours(img,[cnt_max],0,(255,0,255),2)
cv2.imshow("dsf",img)
cv2.waitKey()
cv2.destroyAllWindows()
