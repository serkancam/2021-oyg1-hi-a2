# veri_gizleme_soyutlama.py
class Araba():
    def __init__(self,renk,marka):
        self.renk=renk
        self.marka=marka
        self.__model=1983
        self.__hiz=190
        self.__vites=5
        self.__fiyat=158000.0

    def model_bilgisi(self):
        return self.__model

    def model_belirle(self,model):
        if model>=1983 and model<=2021:
            self.__model=model

a1=Araba("mavi","BMW")
a1.model_belirle(1986)
print(a1.model_bilgisi())
