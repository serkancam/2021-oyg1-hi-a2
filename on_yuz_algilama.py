import cv2
import numpy as np
import os
casc_yol = os.path.join(os.getcwd(),"images","chp2","haarcascade_frontalface.xml")
yuz_casc = cv2.CascadeClassifier(casc_yol)
cap = cv2.VideoCapture(0)
while True:
    ret,resim= cap.read()    
    griTon = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_casc.detectMultiScale(griTon, 1.3, 5)
    for (x, y, w, h) in yuzler:
        cv2.rectangle(resim, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imshow('yuzler', resim)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()