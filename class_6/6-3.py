import cv2

img  = cv2.imread("lenna.jpg")

up_left  = img[0:50,0:50].copy()
down_right = img[250:300,250:300].copy()

img[0:50,0:50] = down_right
img[250:300,250:300] = up_left

cv2.imshow("aa",img)
cv2.waitKey()