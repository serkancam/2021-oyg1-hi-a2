import cv2
import numpy as np
import os

resim_yolu=os.path.join(os.getcwd(),"images","chp2","zebra.png")
resim=cv2.imread(resim_yolu)

h,w,c=resim.shape
aspect=w/h
h_new=int(h/2)
w_new=int(h_new*aspect)
dimension = (w_new,h_new)
resim_r1=cv2.resize(src=resim,dsize=dimension,interpolation=cv2.INTER_CUBIC)
resim_r2=cv2.resize(src=resim,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)

print("normal",resim.shape)
print("r1",resim_r1.shape)
print("r2",resim_r2.shape)


cv2.imshow("normal",resim)
cv2.imshow("resim r1",resim_r1)
cv2.imshow("resim r2",resim_r2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# INTER_LINEAR: Bu aslında en yakın dört komşunun (2 × 2 = 4) belirlendiği ve bir sonraki pikselin değerini belirlemek için ağırlıklı ortalamasının hesaplandığı bir çift doğrusal enterpolasyondur. 

# INTER_NEAREST: Bu, o noktanın etrafındaki noktalarda (komşu) noktalarda o fonksiyonun değeri verildiğinde, bir boşluktaki bir olmayan nokta için bir fonksiyonun değerini tahmin etmek için en yakın komşu enterpolasyon yöntemini kullanır. Başka bir deyişle, bir pikselin değerini hesaplamak için, en yakın komşusunun enterpolasyon fonksiyonuna yaklaştığı kabul edilir. 

# INTER_CUBIC: Bu, piksel değerini hesaplamak için bikübik enterpolasyon algoritması kullanır. Çift doğrusal enterpolasyona benzer şekilde, bir sonraki pikselin değerini belirlemek için 4 × 4 = 16 en yakın komşuyu kullanır. Hız bir sorun olmadığında, bikübik enterpolasyon, çift doğrusal ile karşılaştırıldığında daha iyi yeniden boyutlandırılmış bir görüntü sağlar. 

# INTER_LANCZOS4: Bu, 8 × 8 en yakın komşu enterpolasyonunu kullanır. 

# INTER_AREA: Piksel değerinin hesaplanması, piksel alanı ilişkisi kullanılarak gerçekleştirilir (OpenCV resmi belgelerinde açıklandığı gibi). Bu algoritmayı hareli olmayan yeniden boyutlandırılmış bir görüntü oluşturmak için kullanıyoruz. Görüntü boyutu büyütüldüğünde, INTER_AREA INTER_NEAREST yöntemine benzer.



