# calcHist
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coinOnDesk.jpg',0)
h,w = img.shape

alpha = np.ones([h,w],dtype='uint8')
temp = np.uint8(img*0.2)
beta = cv2.add(np.uint8(img*0.2),alpha*120)

cv2.imshow('img',img)
cv2.imshow('temp',temp)
cv2.imshow('img2',beta)

histimg = cv2.calcHist([img],[0],None,[256],[0,256])
histbeta = cv2.calcHist([beta],[0],None,[256],[0,256])

plt.subplot(2,1,1)
# plt.plot(histimg)
plt.bar(range(0,256),histimg[:,0])

plt.subplot(2,1,2)
# plt.plot(histbeta)
plt.bar(range(0,256),histbeta[:,0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()