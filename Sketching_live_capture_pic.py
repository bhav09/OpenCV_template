import cv2
import numpy as np
import warnings


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


video = cv2.VideoCapture(0)
video.set(3,500)
video.set(4,500)
video.set(10,100)
while True:
    _,img = video.read()
    img_flip = cv2.flip(img,1) #flipping the image
    cv2.imshow('Video',img_flip)
    if cv2.waitKey(1) == 27:
        image = img_flip
        break
video.release()
cv2.destroyAllWindows()

#cv2.imshow('Captured Image',image)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_gray_inv = 255 - img_gray
img_neg = 255 - img
style = cv2.imshow('Style',cv2.stylization(img,sigma_s=100,sigma_r=0.25))
result,result1 = cv2.pencilSketch(img,sigma_s=60,sigma_r=0.05,shade_factor=0.1)
#cv2.imshow('Pencil',result)
#cv2.imshow('Another',result1)

stack = stackImages(0.5,([image,img_gray,img_gray_inv],[img_neg,result,result1]))
cv2.imshow('Stack',stack)
cv2.waitKey(0)


