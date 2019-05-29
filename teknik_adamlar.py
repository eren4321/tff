import mysql.connector
from selenium import webdriver
from bs4 import BeautifulSoup
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


klupadi=["Akhisar",
"aytemiz",
"Antalyaspor",
"Beşiktaş",
"Bursaspor",
"BÜYÜKŞEHİR BELEDİYE",
"Çaykur Rizespor",
"Fenerbahçe",
"Galatasaray",
"Göztepe",
"MEDİPOL BAŞAKŞEHİR",
"Kasımpaşa",
"İSTİKBAL MOBİLYA",
"ATİKER KONYASPOR",
"MKE Ankaragücü",
"DEMİR GRUP ",
"Trabzonspor",
"EVKUR YENİ ",
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
"GAZİŞEHİR GAZİANTEP",
"Gençlerbirliği",
"Giresunspor",
"Hatayspor",
"İstanbulspor",
"KARDEMİR KARABÜKSPOR",
"Osmanlıspor",
"Ümraniyespor",
"KONYA ANADOLU",
"Bandırmaspor",
"BAK SPOR KULÜBÜ",
"Darıca ",
"ETİMESGUT",
"Fatih Karagümrük",
"Fethiyespor",
"Kahramanmaraşspor",
"Kırklarelispor",
"MANİSA BÜYÜKŞEHİR",
"MENEMEN BELEDİYE",
"Pendikspor",
"SİVAS BELEDİYE",
"Şanlıurfaspor",
"Tarsus İdman",
"Tokatspor",
"Tuzlaspor",
"Zonguldak Kömürspor",
"Amed",
"Ankara Demirspor",
"Bayrampaşa",
"BODRUM BELEDİYESİ",
"Eyüpspor",
"Gaziantepspor",
"Gümüşhanespor",
"Hacettepe",
"İnegölspor",
"Kastamonuspor",
"Keçiörengücü",
"Manisaspor",
"Niğde Anadolu",
"Sakaryaspor",
"YILPORT SAMSUNSPOR",
"SANCAKTEPE BELEDİYE",
"Sarıyer",
"Utaş Uşakspor",]


#//*[@id="ctl00_MPane_m_163_864_ctnr_m_163_864_txtTakimAdi"]
for ad in klupadi :
    browser.get("http://www.tff.org/default.aspx?pageID=163")

    klube_gore = browser.find_element_by_xpath(
        "//*[@id='ctl00_MPane_m_163_864_ctnr_m_163_864_RadTabStrip1_Tab2']/span/span")
    klube_gore.click( )

    klup_adi=browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_163_864_ctnr_m_163_864_txtTakimAdi']")
    klup_adi.send_keys(ad)

    ara = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_163_864_ctnr_m_163_864_Button1']")
    ara.click( )




    wait = WebDriverWait(browser, 30)
    browser.execute_script("window.scrollTo(0, 800)")
    while True:

            a = browser.page_source
            soup = BeautifulSoup(a, "lxml")
            teknikadamlar = soup.find("table", attrs={"class": "MasterTable_TFF_Contents"})
            e = teknikadamlar.find("tbody")
            table_rows = e.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text.strip() for i in td]
                print(row)


                if row[0] != "Seçilen sezon için uygun kayıt yok.":
                    links = []
                    for link in tr.findAll('a'):
                        links.append(link.get('href'))

                    sql = "INSERT INTO  teknikadam (link ,ad_soyad ,takım  ,gorevi  ,sozlesmebaslangic ,sozlesmebitis,fesih ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    val = (str(links[0]), str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
                    mycursor.execute(sql, val)

                    mydb.commit( )

                    print(mycursor.rowcount, "record inserted.")

                else:
                    continue

            try:
                browser.find_element_by_link_text(") Sonraki »").click( )
                time.sleep(1)

            except NoSuchElementException:
                break

