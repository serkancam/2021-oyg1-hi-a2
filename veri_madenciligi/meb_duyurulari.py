from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.select import Select#açılır menüde seçim
from bs4 import BeautifulSoup
import pandas as pd
import time
ayarlar = FirefoxOptions()
# ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(
    options=ayarlar, executable_path="/home/serkan/Belgeler/2021-oyg1-hi-a2/geckodriver")
surucu.get("http://www.meb.gov.tr/meb_duyuruindex.php")
### açılır menüde seçim####
secim=Select(surucu.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div/div/div[1]/div[1]/div/label/select"))
secim.select_by_value("100")
### açılır menüde seçim####
aciklama = []
tarih = []
adres = []
# icerik = surucu.page_source
# print(icerik)
sayfa=1
son_sayfa=61
while sayfa<=son_sayfa:
    #içerikteki veriye ulaşma
    icerik = surucu.page_source
    agac = BeautifulSoup(icerik,"lxml")
    duyurular = agac.find_all("tr",attrs={"role":"row"})
    # print(duyurular)
    for duyuru in duyurular:
        try:
            duyuru_baslik = duyuru.find_all("td")[1].text
            duyuru_adres=duyuru.find_all("td")[1].find("a").get("href")
            duyuru_tarih= duyuru.find_all("td")[2].text
            adres.append(duyuru_adres)
            aciklama.append(duyuru_baslik)
            tarih.append(duyuru_tarih)
        except:
            continue


    surucu.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[9]/a").click()
    sayfa=sayfa+1
surucu.close()
# print(tarih)
veri = {"tarih":tarih,"adres":adres,"aciklama":aciklama}
df = pd.DataFrame(veri)
# print(df)
df.to_csv("meb_duyurular.csv",index=False)

print("işlem bitti.")