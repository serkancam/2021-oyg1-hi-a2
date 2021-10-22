# kullanıcının girdiği metindeki sert sessiz sayısını bulup sonucu ekrana yazdıran programı yazınz

metin = input("metni giriniz:")
sert_sessizler="fstçkşhpFSTÇKŞHP"
sert_sessiz_sayisi=0

for harf in metin:
    if harf in sert_sessizler:
        sert_sessiz_sayisi+=1
print(sert_sessiz_sayisi)