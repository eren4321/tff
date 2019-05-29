import mysql.connector
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
data = sqlite3.connect("database.db")
imlec=data.cursor()


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

    klube_gore = browser.find_element_by_xpath(
        "//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_tabArama_Tab3']/span/span")

    klube_gore.click()

    klub_adi = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_txtKulupAdi']")
    klub_adi.send_keys(ad)



    # //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2"]
    ara = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2']")
    ara.click()




    wait = WebDriverWait(browser, 30)
    browser.execute_script("window.scrollTo(0, 800)")
    while True:

            a = browser.page_source
            soup = BeautifulSoup(a, "lxml")
            tablo = soup.find("table", attrs={'class': 'MasterTable_TFF_Contents'})
            e = tablo.find("tbody")
            table_rows = e.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text.strip() for i in td]
                sql = "INSERT INTO  oyuncular (LisansNo ,AdSoyad ,DogumYeri ,DogumTarihi ,KulüpTakım ,Statü ,sBaşlangicTarihi ,sBitisTarihi  ,LVerilisTarihi ,YurtDışınaÇıkısTarihi ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
                val = (str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]))
                mycursor.execute(sql, val)

                mydb.commit( )

                print(mycursor.rowcount, "record inserted.")


            try:
                browser.find_element_by_link_text(") Sonraki »").click( )
                time.sleep(1)

            except NoSuchElementException:
                break