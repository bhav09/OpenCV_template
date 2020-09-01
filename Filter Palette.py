import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


kernel = (9,9)
img = cv2.imread('bears_0.10_noisy.jpg')
#img = cv2.resize(img,(205,259)) #resizing
#cv2.imshow('Original',img)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #converting the image to HSV
#cv2.imshow('HSV',img_hsv)

                                #Mean Filter
blur_hsv = cv2.blur(img_hsv,kernel) #blurring the HSV
#cv2.imshow('Blur',blur_hsv)
gray_blur = cv2.blur(img_gray,kernel) #Mean filter in gray

mean_filter = cv2.cvtColor(blur_hsv,cv2.COLOR_HSV2BGR) #Converting HSV to BGR
#cv2.imshow('Mean Filter',mean_filter)

                                #Gaussian Fitler
blur_gauss = cv2.GaussianBlur(img_hsv,kernel,0)
#cv2.imshow('Gaussian Blur',blur_gauss)
gauss_filter = cv2.cvtColor(blur_gauss,cv2.COLOR_HSV2BGR)
gray_gauss = cv2.GaussianBlur(img_gray,kernel,0)
#cv2.imshow('Gaussian FIlter',gauss_filter)

                                #Median Filter
blur_med = cv2.medianBlur(img_hsv,9)
median_filter = cv2.cvtColor(blur_med,cv2.COLOR_HSV2BGR)
gray_med = cv2.medianBlur(img_gray,9)
#cv2.imshow('Median Filter',mean_filter)

#stacking images
stack = stackImages(0.5,([img,img_hsv,blur_hsv],[mean_filter,median_filter,gauss_filter]))
cv2.imshow('Stacked',stack)

stack_gray = stackImages(0.5,([mean_filter,median_filter,gauss_filter],[gray_blur,gray_gauss,gray_med]))
cv2.imshow('Filters in Gray',stack_gray)
cv2.waitKey(0)