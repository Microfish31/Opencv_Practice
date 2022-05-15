# equalizeHist
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coinOnDesk_lowC.jpg')

b,g,r = cv2.split(img)

b = cv2.equalizeHist(b)
g = cv2.equalizeHist(g)
r = cv2.equalizeHist(r)

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

b_h = cv2.calcHist([b],[0],None,[256],[0,256])
g_h = cv2.calcHist([g],[0],None,[256],[0,256])
r_h = cv2.calcHist([r],[0],None,[256],[0,256])

plt.subplot(3,1,1)
plt.bar(range(0,256),b_h[:,0])

plt.subplot(3,1,2)
plt.bar(range(0,256),g_h[:,0])

plt.subplot(3,1,3)
plt.bar(range(0,256),r_h[:,0])

plt.show()

img_merged = cv2.merge([b,g,r])
cv2.imshow("img_merged",img_merged)

cv2.waitKey(0)
cv2.destroyAllWindows()