import random
boyut = random.randint(5,13)
dizi=[]
for i in range(boyut):
    tut=random.randint(1,100)
    dizi.append(tut)
print("siralama başladı")
dizi.sort()
print("sirlama")
print(dizi)
# dizi
# boyut=dizi boyunu bul
# t=boyut//2
# ortanca=0
# eğer sayı tekse:
# 	ortanca=dizi[t]
# değilse:
# 	ortanca=(dizi[t]+dizi[t-1)/2
