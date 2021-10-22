#in anahtar kelimesi(operatör)

print("a" in "ali")
print("A" in "ali")
print("ali" in "merhaba talim terbiye kurulu.")


ad="ali"
metin="ali bugün bize geldi. "
if ad in metin:
    print("evet var.")

sesli_harfler="euıoüaiöEUIOÜAİÖ"
harf="t"
if harf in sesli_harfler:
    print(f"{harf} sesli harftir.")
else:
    print(f"{harf} sessiz harftir.")


hece_sayisi=0
for harf in metin:
    if harf in sesli_harfler:
        hece_sayisi+=1
print(hece_sayisi)