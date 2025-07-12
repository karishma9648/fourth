import cv2

img = cv2.imread("C:\\Users\\Dell\\OneDrive\\Desktop\\NIELIT\\Computer Vision\\Image work\\children.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
haar_caascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_rect = haar_caascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
print(faces_rect)
for (x, y, w, h) in faces_rect:
    print(x,y,w,h)#50,47,132,132
    cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), thickness=2)
    
cv2.imshow('Detected faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()