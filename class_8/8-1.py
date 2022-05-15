import cv2
import numpy as np

img_shape = [300,300,3]
img_black = np.zeros(img_shape,dtype = "uint8")

temp = img_black.copy()
b_circle = cv2.circle(temp,(180,150),50,(255,0,0),-1)
temp = img_black.copy()
g_circle = cv2.circle(temp,(120,150),50,(0,255,0),-1)
temp = img_black.copy()
r_circle = cv2.circle(temp,(150,100),50,(0,0,255),-1)

img = cv2.addWeighted(b_circle,1,g_circle,1,0)
img = cv2.addWeighted(img,1,r_circle,1,0)
# img = cv2.add(b_circle,g_circle)
# img = cv2.add(img,r_circle)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()