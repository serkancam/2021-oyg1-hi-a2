import random
dizi=[]
for a in range(9):
    tut=random.randint(1,100)
    dizi.append(tut)
print(dizi)
sirali=list()
while len(dizi)!=0:
    enk=dizi[0]
    yer=0
    for i in range(len(dizi)):
        if dizi[i]<enk:
            yer=i
            enk=dizi[i]
    deger=dizi.pop(yer)
    sirali.append(deger)
print(sirali)