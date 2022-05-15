import cv2
import numpy as np

img = cv2.imread('coinOnDesk.jpg',0)

h,w = img.shape

# cv2.circle(img,(w,h),20,(0,0,255),-1)
cv2.circle(img,(105,125),5,(0,0,255),2)
cv2.circle(img,(433,125),5,(0,0,255),2)
cv2.circle(img,(35,305),5,(0,0,255),2)
cv2.circle(img,(535,305),5,(0,0,255),2)

src = np.array([[105,125],[433,125],[35,305],[535,305]],np.float32)
dest = np.array([[135,35],[435,35],[135,305],[435,305]],np.float32)
p = cv2.getPerspectiveTransform(src,dest)
r = cv2.warpPerspective(img,p,(w,h))

cv2.imshow('img1',img)
cv2.imshow('img2',r)
cv2.waitKey(0)
cv2.destroyAllWindows()

