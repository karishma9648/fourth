# reading image
import cv2

img = cv2.imread("C:\\Users\\Dell\\Downloads\\daredevil.jpg", 1)
print(type(img))
dimension = img.shape
height = img.shape[0]
width = img.shape[1]
channel = img.shape[2]
size1 = img.size
pixel = height*width

print("Image dimension: ",dimension)
print("Height of image: ",height)
print("Width of image: ",width)
print("No. of channels is: ",channel)
print("Size of image: ",size1)
print("Total no. of pixels is: ",pixel)