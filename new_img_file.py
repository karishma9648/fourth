# using one file we will amke a new file
import cv2
img = cv2.imread("C:\\Users\\Dell\\Downloads\\daredevil.jpg", 0)
print(img)
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("C:\\Users\\Dell\\OneDrive\\Desktop\\NIELIT\\Computer Vision\\dd2.jpg",img)