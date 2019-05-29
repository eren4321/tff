import io

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


oyunculink=[]
a = open("oyunculinkhareket.txt", "r", encoding="utf-8")
for line in a:
    oyunculink.append(line)
count = 10148
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
                row = [i.text.strip( ) for i in td]
                if row[0] != "Seçilen sezon için uygun kayıt yok.":
                    count += 1
                    sql = "INSERT INTO  hareket (num ,lisansNo,takım  ,baslangıctarihi,bitistarihi ,lisansturu,lisansverilistarihi,yurtdısınacıkıs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (
                        str(count), str(isim2), str(row[0]), str(row[1]),str(row[2]), str(row[3]), str(row[4]), str(row[5]))
                    mycursor.execute(sql, val)

                    mydb.commit()

                    print(mycursor.rowcount, "record inserted.")

                else:
                    continue

            try:
                browser.find_element_by_link_text(") Sonraki »").click( )
                time.sleep(1)

            except NoSuchElementException:
                break