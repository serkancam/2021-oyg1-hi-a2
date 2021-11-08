def yamuk_cevresi(a,b,c=11,d=17):
    cevre=a+b+c+d
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
    print(30*"*")

    return cevre

# fonksiyona (parametre geçme) parametre gönderme yöntemi python da 2 şekilde olur.
#1- pozisyona dayalı
#2- isme dayalı

# 1-poziyona dayalı
c1=yamuk_cevresi(2,3,5,6)
# 2-isme dayalı
c2=yamuk_cevresi(c=10,a=8,d=3,b=4)
#3- karışık

# c3=yamuk_cevresi(3,c=5,5,8) eğer bir parametre isme dayalı gönderilirse artık pozisyona dayalı parametre gönderimi kullanılamaz.(soldan sağa akışta)
c3=yamuk_cevresi(3,c=11,b=5,d=8) 
# c4=yamuk_cevresi(3,c=11,a=5,d=8) #hatalı
c4=yamuk_cevresi(a=3,b=5,c=101)