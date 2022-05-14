import cv2
import os

# yol=os.path.join(os.getcwd(),"images","chp2","elmalar3.jpg")
# yol=os.path.join(os.getcwd(),"images","chp2","sekil_geo.jpg")
yol=os.path.join(os.getcwd(),"images","chp2","rice_1.jpg")
# yol=os.path.join(os.getcwd(),"images","chp2","elma.png")
goruntu=cv2.imread(yol)
gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
gri=cv2.GaussianBlur(gri,(3,3),0)
# gri=cv2.bilateralFilter(gri,5,200,150)
# _,sb=cv2.threshold(gri,20,255,cv2.THRESH_BINARY)
# sb=cv2.erode(sb,None,iterations=3)
sb=cv2.Canny(gri,40,180)
konturlar,_=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
orj=goruntu.copy()
print(len(konturlar))

for kontur in konturlar:
    deger=cv2.approxPolyDP(kontur,0.009*cv2.arcLength(kontur,True),True)
    cv2.drawContours(goruntu,[deger],0,(0,0,0),2)
cv2.imshow("sonuc",goruntu)
cv2.imshow("orj",orj)
cv2.waitKey(0)
cv2.destroyAllWindows()