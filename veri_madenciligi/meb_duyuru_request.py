from bs4 import BeautifulSoup
import requests
import pandas as pd

liste = []

a = 1
while a<=2:
    r = requests.get("http://www.meb.gov.tr/meb_duyuruindex.php")
    agac = BeautifulSoup(r.content,"lxml")
   
    duyurular = agac.find_all("tr",attrs={"role":"row"})
    print(duyurular)
    for duyuru in duyurular:
        # print(duyuru)
        try:
            duyuru_baslik = duyuru.find_all("td")[1].text
            duyuru_adres=duyuru.find_all("td")[1].find("a").get("href")
            duyuru_tarih= duyuru.find_all("td")[2].text
            print(duyuru_adres)
        except:
            continue    


    a = a+1