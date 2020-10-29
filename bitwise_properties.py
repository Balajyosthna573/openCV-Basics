import cv2
import numpy as np
import datetime


img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300,100), (255,255,255))

img2 = cv2.imread('sample2.jpg')

img = cv2.resize(img1, (512,512))
img1 = cv2.resize(img2, (512,512))
bitAnd = cv2.bitwise_and(img1, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.imshow('bitand', bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()