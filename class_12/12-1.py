import cv2

img = cv2.imread("A4paper70cm.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

a,thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)

# edged = cv2.Canny(thresh,35,125)
# cv2.imshow("edged",edged)

contour,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

area_max = -1
area_max_index = -1

for i in range(len(contour)) :
    area = cv2.contourArea(contour[i])
    if (area>area_max) :
        area_max = area
        area_max_index = i

cv2.drawContours(img,contour,area_max_index,(255,0,255),2)
cv2.imshow("dsf",img)
cv2.waitKey()
cv2.destroyAllWindows()
