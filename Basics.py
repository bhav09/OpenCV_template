#loading image and displaying image using open cv
#agar desktop pe h to sidha daal do
import cv2

#when the image is not present on the desktop
img = cv2.imread("C:/Users/91884/Pictures/images.jpg",1)
cv2.imshow('Desktop Image', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
#size of the first image
print('Size of image one is:', img.shape)

#when the image is present on desktop , you still have to give the location
img_2=cv2.imread('C:/Users/91884/Desktop/image.jpg')
cv2.imshow('Desktop Image', img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('Size of image two is:', img_2.shape)