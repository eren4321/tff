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
data = sqlite3.connect("database.db")
imlec=data.cursor()



oyunculink=[]
a = open("teknikadam_link.txt", "r", encoding="utf-8")
for line in a:
    oyunculink.append(line)
count = 0

for ad in oyunculink :
    browser.get("http://www.tff.org.tr/%s"%ad)
    a = browser.page_source
    soup = BeautifulSoup(a, "lxml")
    isim = soup.find("table", attrs={'id': 'ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_oyuncuLisansBilgileri'})
    isim1 = isim.find("span", attrs={'id': 'ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_oyuncuLisansBilgileri_Label4'})
    if isim1 is None:
        continue
    else :
        isim2 = isim1.text

    maclar = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_RadTabStrip1_maclar']/span/span")

    maclar.click()


    yil = ["ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c1",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c2",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c3",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c4",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c5",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c6",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c7",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c8",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c9",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c10",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c11",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c12",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c13",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c14",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c15",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c16",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c17",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c18",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_c19"]
    for yıl in yil:
        time.sleep(1)
        combobox = browser.find_element_by_xpath(
            "//*[@id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector2_combo_Image']")
        combobox.click( )


        sn = browser.find_element_by_id("%s" % yıl)
        sn.click()



        wait = WebDriverWait(browser, 30)
        browser.execute_script("window.scrollTo(0, 800)")
        while True:

                a = browser.page_source
                soup = BeautifulSoup(a, "lxml")
                if soup.find("table", attrs={'class': 'MasterTable_TFF_Contents'}):
                    tablo = soup.find("table", attrs={'class': 'MasterTable_TFF_Contents'})
                    e = tablo.find("tbody")
                    table_rows = e.find_all('tr')

                    for tr in table_rows:
                        td = tr.find_all('td')
                        row = [i.text.strip( ) for i in td]
                        print(row)
                        if row[0] != "Seçilen sezon için uygun kayıt yok." :
                            count += 1
                            sql = "INSERT INTO  maclar (num,lisansNo ,evsahibitakım ,skor,misafirtakım,tarihsaat,organizasyon) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                            val = (
                                str(count),str(isim2), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
                            mycursor.execute(sql, val)

                            mydb.commit()

                            print(mycursor.rowcount, "record inserted.")

                        else:
                            continue

                    try:
                        browser.find_element_by_link_text(") Sonraki »").click()
                        time.sleep(1)

                    except NoSuchElementException:
                        break


