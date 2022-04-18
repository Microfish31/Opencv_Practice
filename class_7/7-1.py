import cv2
import numpy as np

class Point () :
    def __init__(self , x,y) :
        self.x = int(x)
        self.y = int(y)

# 畫布
img1 = np.full((300,300,3),(255,255,255),np.uint8)
r = 100
radians = np.linspace(0,360,1000)* np.pi / 180
center = Point(150,150)

x = np.uint16(center.x + r * np.cos(radians))
y = np.uint16(center.y + r * np.sin(radians))

img1[x,y,:] = [255,0,0]

cv2.imshow("img",img1)
cv2.waitKey()

#img2 = np.uint8(np.zeros([300,300,3]))
#img2[:,:,2] = 200