# kullanıcının girdiği sayının collatz hipotezi yardımı ile 1'e dönmesini sağlayan kodu yazınız
# ve her adımda oluşan değeri ekrana yazdırınız.
# sayı çift ise ikiyi bölün
# tek ise 3 ile çarpıp 1 ekleyin

sayi=int(input("sayı giriniz:"))
adim=1
while sayi!=1:
    if sayi%2==0:
        sayi=sayi//2
    else:
        sayi=sayi*3+1
    print(f"{adim}. adım={sayi}")
    adim+=1