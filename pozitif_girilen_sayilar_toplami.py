# pozitif_girilen_sayilar_toplami.py
# kullanıcı negatif sayı girene kadar olan bütün sayıların toplamını bulan programın kodunu yazınız.

# toplam=0
# while True:
#     sayi=float(input("sayı giriniz:"))
#     if sayi<0:
#         break
#     toplam=toplam+sayi

# print(toplam)
#kullanıcının girdiği pozitif tek tam sayıları toplayan 0 değeri girilince toplam sonucunu ekrana yazan kodu yazınız.

toplam=0
while True:
    sayi=float(input("sayı giriniz:"))
    if sayi==0:
        break
    elif sayi%2==0:
        continue
    toplam=toplam+sayi 
# while True:
#     sayi=float(input("sayı giriniz:"))
#     if sayi<0:
#         break
#     toplam=toplam+sayi 
print(toplam)