# opening image using condition
import cv2
import numpy as np
import sys
img = cv2.imread(cv2.samples.findFile("C:\\Users\\Lenovo\\Downloads\\pic20250226022902.jpg"))
if img is None:
    sys.exit("Module not found")
cv2.imshow("original-----",img)
k=cv2.waitKey(0)
print(k)
if k == ord("s"):
    cv2.imwrite("C:\\Users\\Lenovo\Downloads\\pic20250226022902.jpg",img)