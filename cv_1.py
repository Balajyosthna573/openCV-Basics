import cv2
import numpy as np
import datetime


print(cv2.__version__);
img = cv2.imread("sample1.jpg", 1)
cv2.imshow("image",img)
k = cv2.waitKey(0) &  0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('sample1_copy.jpg', img)
    cv2.destroyAllWindows()
print(img)

