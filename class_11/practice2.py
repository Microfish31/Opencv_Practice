import cv2
import numpy as np

img = np.zeros([300,300])

cv2.rectangle(img,(50,50),(100,100),(255,0,0),-1)
cv2.circle(img,(200,200),30,(255,0,0),-1)
cv2.imwrite("practice2.jpg",img)

img0518 = cv2.imread("practice2.jpg")

edge = cv2.Canny(img0518,100,200)

cv2.imshow("origin",img0518)
cv2.imshow("eg",edge)
# pos = np.where(edge>200)
cv2.waitKey(0)
cv2.destroyAllWindows()