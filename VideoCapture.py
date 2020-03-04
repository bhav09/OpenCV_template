import cv2,time
#zero means only the webcam
video=cv2.VideoCapture(0)
cv2.waitKey(0)
time.sleep(3)
video.release()