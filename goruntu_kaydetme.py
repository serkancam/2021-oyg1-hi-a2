import cv2
import numpy as np
import os

resim=np.zeros((400,400,3),dtype=np.uint8)
rg=np.random.randint(0,255,(400,400,3),dtype=np.uint8)

# ekranın tam ortasına yarıçapı 40 px, mavi renkli kenarı olan ve kenar kalınlığı 3 piksel olan bir çember çiziniz.
# Bu çemberi tam olarak kaplayan kırmızı renkli 3 piksel kenar kalınlığına sahip bir kare çiziniz.
cv2.circle(resim,(200,200),40,(255,0,0),3)
cv2.rectangle(resim,(160,160),(240,240),(0,0,255),3)

cv2.imshow("resim",resim)
cv2.imshow("rastgele",rg)
cv2.waitKey(0)
cv2.destroyAllWindows()

dosya_yolu = os.path.join(os.getcwd(),"images","chp1","calisma1.png")
cv2.imwrite(dosya_yolu,resim)
