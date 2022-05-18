import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_,frame1=cap.read()
_,frame2=cap.read()

while True:
    fark = cv2.absdiff(frame1,frame2)
    gri = cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    _,sb =cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
    yayilmis=cv2.dilate(sb,None,iterations=3)
    
    # print(np.count_nonzero(yayilmis))

    #1. yol siyah olmayan piksellerin sayısı 10.000 den fazla ise ekrana hareket algilandi yaz
    if np.count_nonzero(yayilmis)>10_000:
        cv2.putText(frame1,"hareket algilandi",(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
    
    #2. yol
    konturlar,_=cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    kopya=frame1.copy()
    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        if cv2.contourArea(kontur)<7000:
            continue
        cv2.rectangle(kopya,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(kopya,"hareket algilandi",(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)

    cv2.imshow("yayilmis",yayilmis)
    cv2.imshow("sonuc1",frame1)
    cv2.imshow("sonuc2",kopya)
    frame1=frame2
    _,frame2=cap.read()

    if cv2.waitKey(20)==27:
        break

cap.release()
cv2.destroyAllWindows()