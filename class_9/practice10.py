import cv2
img = cv2.imread("lenna.jpg")

while 1:
    cv2.imshow("fff",img)

    key = cv2.waitKey(1000) & 0xFF

    print(key)

    if key == ord("q"):
        break