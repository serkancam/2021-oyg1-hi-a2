import cv2
import numpy as np
import os

# yol=os.path.join(os.getcwd(),"images","yuz.jpg")
yol=os.path.join(os.getcwd(),"images","chp2","scanned_doc.png")
goruntu=cv2.imread(yol)
# gri dönüşüm
gri = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
# siyah beyaz dönüşüm
t,sb1=cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
t,sb2=cv2.threshold(gri,60,255,cv2.THRESH_BINARY_INV)
erode=cv2.erode(sb1,None,iterations=1)
dilate=cv2.dilate(sb1,None,iterations=1)
print(goruntu.shape)
print(gri.shape)
cv2.imshow("renkli",goruntu)
cv2.imshow("gri",gri)
cv2.imshow("sb1",sb1)
cv2.imshow("sb2",sb2)
cv2.imshow("erode",erode)
cv2.imshow("dilate",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
