import random
dizi=list()#[]
for a in range(10):
    tut=random.randint(1,100)
    dizi.append(tut)

print(dizi)

enk=dizi[0]
yer=0
for i in range(len(dizi)):
    if dizi[i]<enk:
        yer=i
        enk=dizi[i]

print(f"en küçük değer={enk} yeri={yer}")


