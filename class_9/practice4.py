# Gaussian filter
import numpy as np
import cv2

img = cv2.imread('lenna_noise.jpg')
dst = cv2.GaussianBlur(img,(5,5),3,3)

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()