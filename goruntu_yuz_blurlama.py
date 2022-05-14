import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"images","yuz.jpg")
goruntu=cv2.imread(yol)
parca=goruntu[30:325,150:420]
parca=cv2.blur(parca,(35,35))
goruntu[30:325,150:420]=parca
cv2.imshow("sonuc",goruntu)
cv2.waitKey(0)
cv2.destroyAllWindows()