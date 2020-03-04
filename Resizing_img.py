import cv2

img = cv2.imread('C:/Users/91884/Desktop/image.jpg',1)
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow('Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
