import cv2
import os
import numpy as np

#resim yolunu(path) bulalım
#marsrover.png
# şuanda bulunduğumuz dizin 
# os.getcwd() şu anda çalışan py dosyasının bulunduğu dizinin tam yolunu(full path) verir
# print(os.getcwd())
cd = os.getcwd()#şu anda b
img_path=os.path.join(cd,"images","chp1","marsrover.png")
#/home/serkan/Belgeler/2021-oyg1-hi-a2/images/chp1/marsrover.png
image = cv2.imread(img_path)

# image verisine ait çeşitli bilgiler
print("image boyutu=",image.ndim)
print("image dizisi şekli=",image.shape)
print("image yükseklik",image.shape[0])
print("image genişlik",image.shape[1])
print("image renk kanal sayısı",image.shape[2])
#
parca1=image[0:200,0:320]
parca2=image[0:200,320:]
parca3=image[200:,0:320]
parca4=image[200:,320:]

# kare çizelim
sol_ust=(100,70)
sag_alt=(350,380)
renk1=(0,255,0)
kl1=2
cv2.rectangle(image,sol_ust,sag_alt,renk1,kl1)
# çember
renk2=(255,0,0)
cv2.circle(image,sol_ust,50,renk2,kl1)
cv2.circle(image,(350,70),50,renk2,kl1)

# image görüntüsü resmim isimli bir pencerede açılacak
cv2.imshow("resmim",image)
cv2.imshow("parca1",parca1)
cv2.imshow("parca2",parca2)
cv2.imshow("parca3",parca3)
cv2.imshow("parca4",parca4)

#benden bir tıklama gelene kadar beklemesi için
cv2.waitKey(0)
cv2.destroyAllWindows()