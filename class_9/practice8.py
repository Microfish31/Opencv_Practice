import numpy as np
import cv2

img1 = cv2.imread("messi5.jpg")
img2 = cv2.imread("messi5p.jpg")

diff = cv2.absdiff(img1,img2)
gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)

a,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

get_white_area = np.where(thresh==255)

X = int(np.average(get_white_area[1]))
Y = int(np.average(get_white_area[0]))

cv2.circle(img1,(X,Y),20,(255,0,0),5)

cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
