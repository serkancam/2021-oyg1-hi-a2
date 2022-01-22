# kullanıcının girdiği sayının tam bölenlerini ekrana yazdıran programı yazınız.

# 15 --> 1 3 5 15-->range(1,16)
# 60 --> 1 2 3 4 5 6 10 12 15 20 30 60--> range(1,61)
# 11 --> 1 11
# 6 --> 1 2 3 6

sayi = int(input("sayı giriniz:"))

for t in range(1,sayi+1):
    if sayi%t==0:
        print(t,end=" ")