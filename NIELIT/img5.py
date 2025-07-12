#Capture Video from Camera
import cv2
#reading own video from webcamp
video = cv2.VideoCapture(0)
# Reading the video from URL
video = cv2.VideoCapture("saurabh1.avi",0)
# Initializing the backgroundsubtractor
background = cv2.createBackgroundSubtractorMOG2()

while(video.isOpened()):
    ret, frame = video.read()

# Resizing the video
    frame = cv2.resize(frame, None,None, fx=0.2, fy=0.2)

# Creating and applying the maskon each frame
    mask = background.apply(frame)
#  print(mask)
    cv2.imshow('frame', mask)
# Using waitKey to display eachframe of the video for 1 ms
    key = cv2.waitKey(100)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
