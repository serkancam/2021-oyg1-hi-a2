# aldığı parametreler ile dikdörtgen çevresini hesaplayıp  sonucu geri döndüren bir fonksiyon tanımlayıp kullanınız.

def dikdortgen_cevre(uk,kk):
    cevre=(kk+uk)*2
    return cevre

# iki sayının karelerinin farkını hesaplayıp sonucu geri döndüren fonksiyonu yazınız.
def kare_fark(s1,s2):
    f=s1**2-s2**2
    return f
a=float(input("kısa kenarı giriniz:"))
b=float(input("uzun keranrı giriniz:"))

c=dikdortgen_cevre(a,b)
print(c)
