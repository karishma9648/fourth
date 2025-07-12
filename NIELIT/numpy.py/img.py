import cv2

import numpy as np

cap=cv2.VideoCapture(0)

while(True):
 
# Capture image frame-by-frameret,
# 
frame=cap.read()
 # Our operations on the frame come here
 gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 # Display the resulting frame
 cv2.imshow('frame',gray)
 if cv2.waitKey(1)& 0xFF==ord('q'):
   break
 # When everything done, release the capture  
cap.release()
cv2.destroyAllWindows()
 #The cap.read() returns a boolean 
value(True/False).
 #It will return True, if the frame is read correctly