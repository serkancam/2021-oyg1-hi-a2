import cv2
kamera = cv2.VideoCapture(2)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    durum,cerceve=kamera.read()
    cerceve=cv2.flip(cerceve,1)
    cv2.circle(cerceve,(300,300),30,(157,198,160),-1)
    cv2.imshow("kamera",cerceve)
    if cv2.waitKey(20)& 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()


