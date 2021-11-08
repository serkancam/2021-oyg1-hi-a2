
# tanımlama
# parametre almayan geriyde değer döndürme
def merhaba():
    print("merhaba sınıf")
#parametre alan geriye değer döndürmeyen
def merhaba2(adet):
    for i in range(adet):
        print("merhaba")

def topla(s1,s2):
    t=s1+s2
    print(t)
def carp(s1,s2):
    c=s1*s2
    return c


merhaba()
merhaba2(3)
a=5
merhaba2(a)
topla(30,40)
s=carp(30,40)
print(s)
print(carp(10,23))
