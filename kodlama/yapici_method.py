class Personel():
    def __init__(self, ad:str="bos", soyad:str="bos", yas:int=1, gorev:str="bos", maas:float=1.0):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.gorev = gorev
        self.maas = maas
    def zam(self, oran: float):
        if oran>0:
            self.maas = self.maas+self.maas*oran
        # self.maas=self.maas*(1+oran)
    def odul(self,miktar:float):
        self.maas+=miktar
    def __del__(self):
        print(self.ad,"silindi")
    



p1 = Personel("ayşe", "gül", 38, "muhasebe", 6900.0)
p5=Personel()
# p1.maas=6800.0
print(p1.ad, p1.soyad, p1.yas, p1.gorev, p1.maas)
p2 = Personel("serkan", "çam", 39, "öğretmen", 5900.0)
print(p2.gorev)
p2.gorev = "bölüm şefi"
p2.maas=p2.maas*1.1
p2.zam(-0.1)
p2.odul(300)
print(p2.gorev)
print(p2.maas)
p1.maas=200.0
p1.zam(0.2)
# del p2
# print(p1.ad)