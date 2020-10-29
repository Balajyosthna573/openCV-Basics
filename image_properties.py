import cv2
import numpy as np
import datetime

img = cv2.imread('sample1.jpg',1)
img1 = cv2.imread('sample2.jpg', 1)

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[210:280, 530:600]
img[190:260, 200:270] = ball
img = cv2.resize(img, (512,512))
img1 = cv2.resize(img1, (512,512))

dst = cv2.addWeighted(img, .9, img1, .3, 0)
dst = cv2.add(img, img1)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()