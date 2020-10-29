import cv2
import numpy as np
import datetime

def nothing(x):
    print(x)


cv2.namedWindow('image')

cv2.createTrackbar('cp', 'image', 10,400, nothing)
switch = 'Color/Gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv2.imread('sample2.jpg')
    pos = cv2.getTrackbarPos('cp', 'image')
    font  = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (50,150), font,5, (0,0,255))
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img  = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    img = cv2.imshow('image', img)
cv2.destroyAllWindows()

