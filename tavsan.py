sayi=int(input("sayı giriniz:"))

t=1
while t<=sayi:
    bs=(sayi-t)*2
    print(t*"*",bs*" ",t*"*",sep="")
    t=t+1

t=t-2
while t>=1:
    bs=(sayi-t)*2
    print(t*"*",bs*" ",t*"*",sep="")
    t=t-1
