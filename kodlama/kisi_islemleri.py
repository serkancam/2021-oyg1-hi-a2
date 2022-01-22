from kisi import Kisi
while True:
    islem = input("(0-okuma,1-kayıt,2-yaş ortalaması,3-çıkış) işlem seç:")
    if islem=="0":
        print("okuma")
        dosya = open("kisiler.txt","r",encoding="utf-8")
        for s in dosya:
            print(s,end="")
        dosya.close()
    elif islem=="1":
        print("kayıt")
        while True:
            try:
                ad=input("ad giriniz:")
                soyad=input("soyad giriniz:")
                yas=int(input("yaş giriniz:"))
            except:
                print("Yaş değeri sayı olmalıdır.")
                continue
            if len(ad)<2 or len(soyad)<2 or yas<0 :
                print("Ad soyad en az 2 karakterli yaş değeri poziti olmalıdır")
                continue

            k=Kisi(ad,soyad,yas)
            k.kayit("kisiler.txt")
            break
    elif islem=="2":
        print("ortalama")
        dosya =open("kisiler.txt","r",encoding="utf-8")
        ort=0
        adet=0
        for s in dosya:
            yas = int(s.split(",")[2].strip())
            ort=ort+yas
            adet=adet+1
        ort = ort/adet
        print(f"yaş ortalaması={ort}")
    elif islem=="3":
        print("çıkış")
        break
    else:
        print("yanlış işlem seçimi!")


