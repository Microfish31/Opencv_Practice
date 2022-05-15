import cv2
from findMarker import findMaxContour as fm
import numpy as np

img_name = "A4paper70cm.jpg"
img = cv2.imread(img_name)
get_max_contour = fm(img)

rect = cv2.minAreaRect(get_max_contour)
box = np.int64(cv2.boxPoints(rect))

cv2.drawContours(img,[box],0,(0,255,0),2)
txt = str(int(rect[1][0])) + ',' + str(int(rect[1][1]))
print(txt)
cv2.putText(img,txt,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
cv2.imshow("dsf",img)
cv2.waitKey()
cv2.destroyAllWindows()