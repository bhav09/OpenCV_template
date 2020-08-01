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


def getContours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500: #giving a threshold so that it doesn't detects noise
            cv2.drawContours(imgcontour,cnt,-1,(0,0,0),5)
            cv2.drawContours(result,cnt,-1,(0,0,0),4)
            perimeter = cv2.arcLength(cnt,True)
            #print(perimeter)
            points = cv2.approxPolyDP(cnt,0.02*perimeter,True) #to find the no of corner points
            print(len(points)) #no of points
            corners = len(points)
            x,y,w,h = cv2.boundingRect(points)
            if corners == 3:
                shape = 'Tri'
            elif corners==4:
                ratio = w/float(h)
                if ratio>0.95 and ratio<1.05:
                    shape = 'Sq'
                else:
                    shape = 'Rect'
            else:
                shape = 'Cir'
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(20,255,50),2)
            cv2.putText(result,shape,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)


img = cv2.imread('shapes.png')
imgcontour = img.copy()
result = img.copy()

#converting them to grayscale so as to ind the corner points
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#now blurring the image
blur = cv2.GaussianBlur(gray,(7,7),0.8)

#to find the edges
canny = cv2.Canny(blur,50,50)

getContours(canny)

blank_image = np.zeros_like(img)
imgstack = stackImages(0.5,([img,gray,blur],[canny,imgcontour,result]))
cv2.imshow('Stack',imgstack)
#cv2.imshow('Contour',imgcontour)
cv2.waitKey(0)