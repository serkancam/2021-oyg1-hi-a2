# 1- kapsülleme-veri gizleme(encapsulation)
# 2- miras(inheritance)
# 3- çok biçimlilik(polymorpyhsm)

class Kisi():#ata sınıf, parent, super()-->java ve python
    def __init__(self,adi,soyadi):
        self.ad=adi
        self.soyad=soyadi
        print("atam")

class Ogrenci(Kisi):
    def __init__(self,ad,soyad,okul_no,sinif):
        super().__init__(ad,soyad)    
        self.okul_no=okul_no
        self.sinif=sinif
        print("torunum")
        
class Ogretmen(Kisi):
    pass

#türetmeler
k1 = Kisi("serdar","kul")
o1=Ogrenci("hasan","kat",185,4)
o2=Ogretmen("mahmut","atadan")
print(k1.ad,k1.soyad)
print(o1.okul_no,o1.sinif,o1.ad,o1.soyad)
print(o2.ad,o2.soyad)

