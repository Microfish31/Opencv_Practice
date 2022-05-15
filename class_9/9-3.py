# Contour

import cv2

# cap = cv2.VideoCapture("test.mp4")
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
f_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(f_num)

for i in range(10):
    ret,frame = cap.read()

    if ret :
      cv2.imshow('frame',frame)
      cv2.waitKey(1000)
cap.release()
cv2.destroyAllWindows()