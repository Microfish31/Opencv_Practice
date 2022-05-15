# Medium value filter
import numpy as np
import cv2

img = cv2.imread('lenna_noise.jpg')
dst = cv2.medianBlur(img,3)

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()