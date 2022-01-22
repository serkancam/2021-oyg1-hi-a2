while True:
    try:
        s1=int(input("1. sayıyı giriniz:"))
        s2=int(input("2. sayıyı giriniz:"))
        sonuc = s1/s2
        print(f"{s1}/{s2}={sonuc}")
        break
    except ValueError:
        print("Girdiğiniz değerler tam sayı değil")
        continue
    except ZeroDivisionError:
        print("Sıfıra bölme hatası. 2. değer sıfır girilemez")
        continue
    except:
        print("hata")
        continue




