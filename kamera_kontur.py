import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    _,goruntu=cap.read()
    # goruntu = cv2.flip(goruntu,1)
    gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    bulanik=cv2.GaussianBlur(gri,(3,3),0)
    # gri=cv2.bilateralFilter(gri,5,200,150)
    # _,sb=cv2.threshold(gri,20,255,cv2.THRESH_BINARY)
    # sb=cv2.erode(sb,None,iterations=3)
    sb=cv2.Canny(bulanik,40,140)
    konturlar,_=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(konturlar))
    mask=np.zeros_like(goruntu)


    

    cv2.drawContours(goruntu,konturlar,-1,(255,0,0),1)
    cv2.drawContours(mask,konturlar,-1,(255,0,0),1)
    out = np.zeros_like(goruntu)
    out[mask == 255] = goruntu[mask == 255]
    # for kontur in konturlar:
    #     deger=cv2.approxPolyDP(kontur,0.009*cv2.arcLength(kontur,True),True)
    #     cv2.drawContours(goruntu,[deger],0,(0,0,0),2)
    cv2.imshow("canyy",sb)
    cv2.imshow("sonuc",goruntu)
    cv2.imshow("out",out)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()