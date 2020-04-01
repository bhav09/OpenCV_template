#dependency for the database
import sqlite3
#establishing a connection
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("drop table users")
c.execute('''CREATE TABLE users (id integer unique primary key autoincrement,name text)''')
print('Table created !')
conn.commit()
conn.close()
import cv2
import numpy as np
import os

#making a folder for storing custom based image data
conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')
c = conn.cursor()

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#to capture frames from the webcam of laptop
cam = cv2.VideoCapture(0)
username = input('Enter Name:')
c.execute("INSERT INTO users (name) VALUES (?)",(username,))
uid = c.lastrowid
sample = 0
while True:
  check, frame = cam.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting each frame to grayscale
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    sample = sample+1
    cv2.imwrite("dataset/User."+str(uid)+"."+str(sample)+".jpg",gray[y:y+h,x:x+w])
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)
  cv2.imshow('Frame',frame)
  cv2.waitKey(1)
  if sample > 25:     #will store 25 frames
    break
cam.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()


from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
if not os.path.exists('./recognizer'):
    os.makedirs('./recognizer')
def getImagesWithID(path):
  imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
  faces = []
  IDs = []
  for imagePath in imagePaths:
    faceImg = Image.open(imagePath).convert('L')
    faceNp = np.array(faceImg,'uint8')
    ID = int(os.path.split(imagePath)[-1].split('.')[1])
    faces.append(faceNp)
    IDs.append(ID)
    cv2.imshow("training",faceNp)
    cv2.waitKey(10)
  return np.array(IDs), faces
Ids, faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainingData.yml')
print('Process Finished')
cv2.destroyAllWindows()


