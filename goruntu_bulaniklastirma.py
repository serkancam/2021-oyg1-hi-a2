import cv2
import numpy as np
import os

yol1=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
yol2=os.path.join(os.getcwd(),"images","chp2","salt-pepper.jpg")
doga=cv2.imread(yol1)
beyin=cv2.imread(yol2)
#mean filter
doga_b1=cv2.blur(doga,(3,3))
doga_b2=cv2.blur(doga,(13,13))
beyin_b1=cv2.blur(beyin,(5,5))
doga_mf1=cv2.medianBlur(doga,9)
#median filter
beyin_mf1=cv2.medianBlur(beyin,3)
beyin_mf2=cv2.medianBlur(beyin,5)

# gaussian blur/filter
doga_gf1=cv2.GaussianBlur(doga,(13,13),0)
beyin_gf1=cv2.GaussianBlur(beyin,(9,9),0)

#görüntüler
cv2.imshow("doga original",doga)
cv2.imshow("doga b1",doga_b1)
cv2.imshow("doga b2",doga_b2)
cv2.imshow("doga mf1",doga_mf1)
cv2.imshow("beyin",beyin)
cv2.imshow("beyin b1",beyin_b1)
cv2.imshow("beyin mb1",beyin_mf1)
cv2.imshow("beyin mf2",beyin_mf2)
cv2.imshow("doga gf1",doga_gf1)
cv2.imshow("beyin gf1",beyin_gf1)

cv2.waitKey(0)
cv2.destroyAllWindows()