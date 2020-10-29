import cv2
import numpy as np
import datetime

img = cv2.imread('sample1.jpg', 1)
img = np.zeros([512,512,3],np.uint8)
img = cv2.line(img, (0,0), (255,255), (255,0,0), 4)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 4)
img = cv2.ellipse(img, (567,257),(80,30),5, 0,360,(0,0,255),10)

pts = np.array([[100,100],[200,300],[700,200],[500,100]],np.int32)
img = cv2.polylines(img, [pts],True,(0,255,255),3)

img = cv2.circle(img, (447,63), 63, (0,255,0), 10)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'openCv', (10,500), font, 4, (255,255,255), 10, cv2.LINE_8)
cv2.imshow('sample', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

