#Write Text and line on Image
import numpy as np
import cv2
f="C:\\Users\\Lenovo\\Downloads\\pic20250226022902.jpg"
font = cv2.FONT_HERSHEY_SIMPLEX
# Create a black image.
img = cv2.imread(f,1)
cv2.putText(img,'mouth',(98,170), font, 1,(255,255,255),2)
cv2.line(img,(10,0),(150,150),(0,80,0),5)
#Display the image
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()