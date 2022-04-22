import cv2 
import numpy as np
import os
from PIL import Image

path1=os.path.join(os.getcwd(),"images","chp2","elma.png")
path2=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
elma=cv2.imread(path1)
doga=cv2.imread(path2)

elma=cv2.resize(elma,(200,200),interpolation=cv2.INTER_AREA)
doga=cv2.resize(doga,(200,200),interpolation=cv2.INTER_AREA)

ekleme1=cv2.add(doga,elma)
ekleme2=elma+doga
cv2.imshow("ekleme1",ekleme1)
cv2.imshow("ekleme2",ekleme2)

cv2.waitKey(0)
cv2.destroyAllWindows()
