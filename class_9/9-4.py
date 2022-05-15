import cv2

img1 = cv2.imread("messi5.jpg")
img2 = cv2.imread("messi5p.jpg")

diff = cv2.absdiff(img1,img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.imshow("diff",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()