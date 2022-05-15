# Find moving
# upload photo
import cv2

cap = cv2.VideoCapture(0)
ret,img1 = cap.read()

cv2.waitKey(1000)

ret,img2 = cap.read()
cap.release()

diff = cv2.absdiff(img1,img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("diff",diff)
cv2.imwrite("moving.jpg",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
