import cv2
import os

cap=cv2.VideoCapture(0)
while True:
    _,image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.Canny(gray, 40,140)

    # Find contour and sort by contour area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    # Find bounding box and extract ROI
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        ROI = image[y:y+h, x:x+w]
        break

    cv2.imshow('ROI',ROI)
    if cv2.waitKey(600)==27:
        break
cap.release()
cv2.destroyAllWindows()