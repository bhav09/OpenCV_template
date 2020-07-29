import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
cam = cv2.imread('Miriam-Ocean-FINAL-NEU-for-web11.jpg')
cam = cv2.resize(cam,(int(cam.shape[1]/2),int(cam.shape[0]/2))) #resizing image

cv2.imshow('Original',cam)

#gray inmae
gray = cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)

#blured image ; used to reduce image noise
blur = cv2.GaussianBlur(cam,(1,1),0)

#canny: used for edge detection
canny = cv2.Canny(cam,200,250)

#morphological operation = dilation and erosion
#dilation:
img_dilate = cv2.dilate(canny,kernel,iterations=1) #iterations=thickness

#erosion:
img_erosion = cv2.erode(img_dilate,kernel,iterations=1)

cv2.imshow('Grayscale',gray)
cv2.imshow('Blur',blur)
cv2.imshow('Canny',canny)
cv2.imshow('Dilation',img_dilate)
cv2.imshow('Erosion',img_erosion)

cv2.waitKey(0)