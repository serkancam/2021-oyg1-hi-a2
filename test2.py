import cv2
import numpy as np

def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)

    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv

    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)

    return imgBack

elma=cv2.imread("/home/serkan/Belgeler/2021-oyg1-hi-a2/images/chp2/elma.png",cv2.IMREAD_UNCHANGED)
doga=cv2.imread("/home/serkan/Belgeler/2021-oyg1-hi-a2/images/chp2/nature.jpg",cv2.IMREAD_UNCHANGED)

elma=cv2.resize(elma,(50,50),interpolation=cv2.INTER_AREA)

sonuc=overlayPNG(doga,elma,[100,100])

cv2.imshow("sonuc",sonuc)
cv2.waitKey(0)


