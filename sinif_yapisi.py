# sinif_yapisi.py
# sınıf içinde tanımlı fonksiyonlar metot adı ile anılır.
# yapıcı metot sınıftan nesne türetilirken çalışan ilk metottur.
# bu metot özel bir metot olup __init__(self) şeklinde tanımlanır.

class Insan():
    def __init__(self):
        self.ad="telli turna"
        self.soyad="bos"
        self.yas=0
        self.kilo=0.0
        self.boy=0.0
        print("merhaba")


#sınıftan insan1 ve insan2 adında iki nesne türettim

insan1=Insan()
insan2=Insan()
insan1.ad="osman"
print(insan1.ad)
# print(Insan.ad) ad özelliği artık sadece sınıftan türetilen nesnelere aittir.
print(insan2.ad)