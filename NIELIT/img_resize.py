#  resizing the image using interpolation method

f ="C:\\Users\\Lenovo\\Downloads\\pic20250226022902.jpg"
import cv2
img=cv2.imread(f,1)
print("Original dimension: ",img.shape)
scale=60 #scaling parameter
height = int(img.shape[0] * scale / 100)
width  = int(img.shape[1] * scale / 100)
dim = (width,height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print("Resized diemnsion: ",resized)
cv2.imshow("Resized image: ",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()