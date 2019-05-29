import mysql.connector
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mydb = mysql.connector.connect(
    host="localhost",
    user="er",
    passwd="eren",
    database="mydata",


)
print(mydb)
mycursor = mydb.cursor()


driver_path = "C:\\Users\erencakir\Desktop\chromedriver.exe"

browser = webdriver.Chrome(driver_path)


klupadi=["Akhisar",
"aytemiz",
"Antalyaspor",
"Beşiktaş",
"Bursaspor",
"BÜYÜKŞEHİR BELEDİYE ERZURUMSPOR",
"Çaykur Rizespor",
"Fenerbahçe",
"Galatasaray",
"Göztepe",
"MEDİPOL BAŞAKŞEHİR FK",
"Kasımpaşa",
"İSTİKBAL MOBİLYA KAYSERİSPOR",
"ATİKER KONYASPOR",
"MKE Ankaragücü",
"DEMİR GRUP SİVASSPOR",
"Trabzonspor",
"EVKUR YENİ MALATYASPOR",
"Adana Demirspor",
"Adanaspor",
"Afjet Afyonspor",
"Altay",
"Altınordu",
"Balıkesirspor",
"Boluspor",
"ABALI DENİZLİSPOR",
"BİREVİM ELAZIĞSPOR",
"Eskişehirspor",
"GAZİŞEHİR GAZİANTEP FUTBOL KULÜBÜ",
"Gençlerbirliği",
"Giresunspor",
"Hatayspor",
"İstanbulspor",
"KARDEMİR KARABÜKSPOR",
"Osmanlıspor",
"Ümraniyespor",
"KONYA ANADOLU SELÇUKSPOR",
"Bandırmaspor",
"BAK SPOR KULÜBÜ",
"Darıca Gençlerbirliği",
"ETİMESGUT BELEDİYESPOR",
"Fatih Karagümrük",
"Fethiyespor",
"Kahramanmaraşspor",
"Kırklarelispor",
"MANİSA BÜYÜKŞEHİR BELEDİYE SPOR	",
"MENEMEN BELEDİYE SPOR",
"Pendikspor",
"SİVAS BELEDİYE SPOR",
"Şanlıurfaspor",
"Tarsus İdman Yurdu",
"Tokatspor",
"Tuzlaspor",
"Zonguldak Kömürspor",
"Amed",
"Ankara Demirspor",
"Bayrampaşa",
"BODRUM BELEDİYESİ BODRUMSPOR",
"Eyüpspor",
"Gaziantepspor",
"Gümüşhanespor",
"Hacettepe",
"İnegölspor",
"Kastamonuspor 1966",
"Keçiörengücü",
"Manisaspor",
"Niğde Anadolu",
"Sakaryaspor",
"YILPORT SAMSUNSPOR",
"SANCAKTEPE BELEDİYE SPOR",
"Sarıyer",
"Utaş Uşakspor",]

for ad in klupadi :
    browser.get("http://www.tff.org.tr/default.aspx?pageID=130")

    # //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_tabArama_Tab3"]/span/span
    time.sleep(5)
    klube_gore = browser.find_element_by_xpath(
        "//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_tabArama_Tab3']/span/span")

    klube_gore.click()
    time.sleep(2)
    klub_adi = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_txtKulupAdi']")
    klub_adi.send_keys(ad)
    time.sleep(2)


    # //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2"]
    ara = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2']")
    ara.click()

    add_oyuncu = ("INSERT INTO tff (LisansNo ,AdSoyad ,DogumYeri ,DogumTarihi ,KulüpTakım ,Statü ,sBaşlangicTarihi ,sBitisTarihi  ,LVerilisTarihi ,YurtDışınaÇıkısTarihi ) VALUES (%d,%s,%s,%d,%s,%s,%d,%d,%d,%d)")


    wait = WebDriverWait(browser, 30)
    browser.execute_script("window.scrollTo(0, 800)")
    while True:
        try:
            a = browser.page_source
            soup = BeautifulSoup(a, "lxml")
            tablo = soup.find("table", attrs={'class': 'MasterTable_TFF_Contents'})
            e = tablo.find("tbody")
            table_rows = e.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row=[]
                for i in td :
                    row.append(i.text.strip())
                    add_oyuncu = ("INSERT into oyuncular (LisansNo ,AdSoyad ,DogumYeri ,DogumTarihi ,KulüpTakım ,Statü ,sBaşlangicTarihi ,sBitisTarihi  ,LVerilisTarihi ,YurtDışınaÇıkısTarihi ) VALUES (" +str(i) + ")")

            time.sleep(3)
            next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, ") Sonraki »")))
            next_button.click()
            time.sleep(3)
        except TimeoutException:
            break
