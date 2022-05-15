# equalizeHist
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coinOnDesk.jpg',0)

equ = cv2.equalizeHist(img)

histgray = cv2.calcHist([img],[0],None,[256],[0,256])
hisequ = cv2.calcHist([equ],[0],None,[256],[0,256])

cv2.imshow("equ",equ)
cv2.imshow("img",img)

plt.subplot(2,1,1)
plt.bar(range(0,256),histgray[:,0])

plt.subplot(2,1,2)
plt.bar(range(0,256),hisequ[:,0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()