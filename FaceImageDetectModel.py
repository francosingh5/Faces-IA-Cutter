import numpy as np
import cv2
import os
import imutils

imgPath = "C:/Users/Tec Barker/Downloads/FacesFound"
if not os.path.exists(imgPath):
    os.makedirs(imgPath)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

image = cv2.imread('PDD_1937.jpg')
imageAux = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

count = 1
scale = 150

for (x,y,w,h) in faces:
    cv2.putText(image, "presione s para almacenar el rostro", (20, 30), 2, 2, (0,0,255),1,cv2.LINE_AA)
    cv2.rectangle(image, (x-scale, y-scale), (x+w+scale, y+h+scale), (0, 255, 0), 5)
    unitFace = imageAux[y-scale:y+h+scale , x-scale:x+w+scale]
    cv2.imshow('image', imutils.resize(image, width=500))
    cv2.imshow('unitFace',unitFace)
    
    k = cv2.waitKey(0)
    
    if(k == ord('s')):
        cv2.imwrite(imgPath + '/' +'PDD_1937_{}.jpg'.format(count), unitFace)
        count = count + 1

print("Imagenes guardadas en: " + imgPath)
cv2.destroyAllWindows()

