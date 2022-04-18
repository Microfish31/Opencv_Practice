import cv2

img = cv2.imread("Lenna.jpg")

cv2.rectangle(img,(20,20),(50,50),(255,0,0),-1)
cv2.circle(img,(35,35),21,(0,255,0),1)
cv2.imshow("img",img)
cv2.waitKey()

cv2.imwrite("Lena_1.jpg",img)