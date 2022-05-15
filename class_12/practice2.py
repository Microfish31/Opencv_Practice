import cv2
from findMarker import findMarkerByFile as fm

img_name = "A4paper70cm.jpg"

get = fm(img_name)

cv2.imshow("get",get)
cv2.waitKey()
cv2.destroyAllWindows()