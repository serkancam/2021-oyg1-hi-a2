import cv2
import numpy as np
import os

img_path=os.path.join(os.getcwd(),"images","chp2","zebrasmall.png")
img=cv2.imread(img_path)
#yatay çevirme
yatay_cevrik=cv2.flip(img,1)
#dikey çevirme
dikey_cevrik=cv2.flip(img,0)
# yatay dikey cevirme,
yatay_dikey_cevrik=cv2.flip(img,-1)

cv2.imshow("orjinal",img)
cv2.imshow("yatay",yatay_cevrik)
cv2.imshow("dikey",dikey_cevrik)
cv2.imshow("yatay_dikey",yatay_dikey_cevrik)
cv2.waitKey(0)
cv2.destroyAllWindows()