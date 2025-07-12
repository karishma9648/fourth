import cv2
import numpy as np

img =cv2.imread("C:\\Users\\Lenovo\\Downloads\\WhatsApp Image 2025-02-03 at 11.50.07 AM.jpeg")
re_img=cv2.resize(img,(600,800))
cv2.imshow("C:\\Users\\Lenovo\\Downloads\\WhatsApp Image 2025-02-03 at 11.50.07 AM.jpeg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()