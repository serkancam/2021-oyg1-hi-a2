# 366 kişilik bir okul gezi grubu 45'er kişi alan otobüsler kiralayarak geziye gidecektir.
# buna göre bu okul en az kaç araç kiralanması gerekir.
# bütün öğrenciler geziye aynı anda farklı araçlar ile katılacaktır. 

kisi_sayisi=366
arac_kisi=45
arac_sayisi=kisi_sayisi//arac_kisi
kalan=kisi_sayisi%arac_kisi

if kalan>0:
    arac_sayisi+=1

print(f"")
