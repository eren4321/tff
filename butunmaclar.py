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
    browser.get("http://www.tff.org/default.aspx?pageID=322")


    klub_adi = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_322_1480_ctnr_m_322_1480_txtKulupAdi']")
    klub_adi.send_keys(ad)
    time.sleep(2)

    yil = ["ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c0",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c1",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c2",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c3",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c4",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c5",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c6",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c7",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c8",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c9",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c10",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c11",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c12",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c13",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c14",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c15",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c16",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c17",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c18",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c19",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c20",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c21",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c22",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c23",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c24",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c25",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c26",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c27",
           "ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_c28" ]
    for yıl in yil:
        combobox = browser.find_element_by_xpath(
            "//*[@id='ctl00_MPane_m_322_1480_ctnr_m_322_1480_SezonSelector3_combo_Image']")
        combobox.click( )
        time.sleep(3)

        sn = browser.find_element_by_id("%s" % yıl)
        sn.click( )

        ara = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_322_1480_ctnr_m_322_1480_btnSave']")
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
                    row = [i.text.strip() for i in td]
                    print(row)
                    maclink = []
                    links = []
                    for link in tr.findAll('a'):
                        links.append(link.get('href'))
                    maclink.append(links[0])
                    print(maclink)

                time.sleep(3)
                next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, ") Sonraki »")))
                next_button.click()
                time.sleep(3)
            except TimeoutException:
                break
