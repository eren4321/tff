import io

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
                oyunculink=[]
                kluplink=[]
                links = []
                for link in tr.findAll('a'):
                    links.append(link.get('href'))
                oyunculink.append(links[0])
                kluplink.append(links[1])
                with io.open('oyunculink.txt', 'a', encoding="utf-8") as f:
                    for item1 in oyunculink:

                        f.write("%s\n" % item1)
                    f.close()
                with io.open('kluplink.txt', 'a', encoding="utf-8") as f:
                    for item2 in kluplink:
                        f.write("%s\n" % item2)
                    f.close()



            time.sleep(3)
            next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, ") Sonraki »")))
            next_button.click()
            time.sleep(3)
        except TimeoutException:
            break
yil = ["2018-2019",
       "2017-2018",
       "2016-2017",
       "2015-2016",
       "2014-2015",
       "2013-2014",
       "2012-2013",
       "2011-2012",
       "2010-2011",
       "2009-2010",
       "2008-2009",
       "2007-2008",
       "2006-2007",
       "2005-2006",
       "2004-2005",
       "2003-2004",
       "2002-2003",
       "2001-2002",
       "2000-2001",
       "1999-2000",
       "1998-1999",
       "1997-1998",
       "1996-1997",
       "1995-1996",
       "1994-1995",
       "1993-1994",
       "1992-1993",
       "1991-1992",
       "1990-1991"]