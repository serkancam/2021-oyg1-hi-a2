import sqlite3 as sql
try:
    no=int(input("no:"))
    ad=input("ad:")
    soyad=input("soyad:")
    sinif=int(input("sınıf:"))
    sube=input("şube:")
    #1- veritabanına bağlan
    vt = sql.connect("/home/serkan/Belgeler/2021-oyg1-hi-a2/veritabani/okul_s.db")
    #2- sql cümleciği kur
    ekle_sql="insert into ogrenci values(?,?,?,?,?)"
    #3- değeleri liste yap
    degerler=[no,ad,soyad,sinif,sube]
    #4- veritabanı işlemleri için bir cursor(imleç) oluştur.
    imlec=vt.cursor()
    #5- veritabanında sql cümleciğini değerler ile çalıştır.(execute)
    imlec.execute(ekle_sql,degerler)
    # ekle-sil-güncelleme işlemleri için işlemler onaylanır. commit()
    vt.commit()
    ####öğrencileri listele##### seçme(select) için commit gerekmez
    sec_sql="select * from ogrenci"
    imlec.execute(sec_sql)
    ogrenciler=imlec.fetchall()
    for ogr in ogrenciler:
        print(f"no:{ogr[0]}-ad:{ogr[1]}-soyad:{ogr[2]}-sınıf:{ogr[3]}-{ogr[4]}")
    ####öğrencileri listele#####
except:
    print("hata")
finally:
    if imlec:
        imlec.close()
    if vt:
        vt.close()