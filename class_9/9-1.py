import cv2
import random

img = cv2.imread('lenna.jpg')

shape = img.shape
numNoise = 2000

for i in range(numNoise) :
    k = random.randint(0,shape[0]-1)
    m = random.randint(0,shape[1]-1)
    img[k,m]=[0,0,0]

cv2.imshow('img',img)
cv2.imwrite('lenna_noise2.jpg',img)

img2 = cv2.imread('lenna_noise2.jpg')
dst = cv2.GaussianBlur(img,(5,5),3,3)
dst2 = cv2.medianBlur(img,3)
cv2.imshow('img2',dst)
cv2.imshow('img3',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()