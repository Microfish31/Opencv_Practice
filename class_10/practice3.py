# find contour
import cv2

img = cv2.imread("img_dilate0422.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow("thr",thr)
cv2.imshow("img",img)

dilated = cv2.dilate(thr,(3,3),iterations=1)

contours,a = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(255,255,0),2)

# print(len(contours))
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()