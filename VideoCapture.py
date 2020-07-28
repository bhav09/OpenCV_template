import cv2
#zero means only the webcam
video = cv2.VideoCapture(0)
video.set(3,500) #for width = 500
video.set(4,500) #for width=500
video.set(10,100) #for brightness=100

while True:
    success,img = video.read()
    img = cv2.resize(img,(int(img.shape[1]*3/4),int(img.shape[0]*3/4)))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img,(9,9),0)
    canny = cv2.Canny(img,150,200)

    cv2.imshow('Original', img)
    cv2.imshow('Gray',gray)
    cv2.imshow('Blur',blur)
    cv2.imshow('Canny',canny)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
