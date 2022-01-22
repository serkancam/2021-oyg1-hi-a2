# veri_gizleme_soyutlama.py
class Araba():
    def __init__(self,renk,marka):
        self.renk=renk
        self.__marka=marka
        self.__model=1983
        self.__hiz=190
        self.__vites=5#4-5-6-7
        self.__fiyat=158000.0#100_000 :: 1_000_000
    
    def marka_belirle(self,marka:str):
        if type(marka) is str:
            print("test")
            self.__marka=marka
    
    def marka_bilgisi(self):
        return self.__marka

    def model_bilgisi(self):
        return self.__model

    def model_belirle(self,model):
        if model>=1983 and model<=2021:
            self.__model=model
    
    def hiz_bilgisi(self):
        return self.__hiz
    
    def hiz_belirle(self,hiz):
        if hiz>=180 and hiz<=400:
            self.__hiz=hiz



a1=Araba("mavi","BMW")
a1.model_belirle(2020)

a1.marka_belirle("5")

print(a1.model_bilgisi())
print(type(a1.marka_bilgisi()))
print(a1.marka_bilgisi())