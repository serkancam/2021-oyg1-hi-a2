import cv2

cap =  cv2.VideoCapture(0)

while True:
    durum,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # t,frame=cv2.threshold(frame,70,255, cv2.THRESH_BINARY_INV)
    _,sb1=cv2.threshold(gri,70,255,cv2.THRESH_BINARY)
    sb2=cv2.adaptiveThreshold(gri,255,cv2.CALIB_CB_ADAPTIVE_THRESH,cv2.THRESH_BINARY_INV,3,3)
    sb3=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,3)
    canny=cv2.Canny(gri,150,250)
    cv2.imshow("sb1",sb1)
    cv2.imshow("sb2",sb2)
    cv2.imshow("sb3",sb3)
    cv2.imshow("canny",canny)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()