# Add noise
import cv2
import random

img = cv2.imread('lenna.jpg')

shape = img.shape
numNoise = 2000

for i in range(numNoise) :
    k = random.randint(0,shape[0]-1)
    m = random.randint(0,shape[1]-1)

    if (len(shape)==2) :
        img[k,m]= 255
    else:
        img[k,m]=[255,255,255]

cv2.imshow('img',img)
cv2.imwrite('lenna_noise.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    