import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('C:/Users/91884/Desktop/herface.jpg')
img_resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#converting to a grayscale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#searching co ordinates in the image(human face)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

#creating face rectangle
for x,y,w,h in faces:
    img_resized=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('Face',img)
    cv2.waitKey(0)
#3= width/thickness of the rectangle
#0,255,0= RGB color scheme , here the rectangle color will be green
