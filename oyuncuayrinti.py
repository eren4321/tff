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


oyunculink=[]
a = open("oyunculink.txt", "r", encoding="utf-8")
for line in a:
    oyunculink.append(line)
    print(line)

for ad in oyunculink :
    browser.get("http://www.tff.org.tr/%s"%ad)

    # //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_tabArama_Tab3"]/span/span
    time.sleep(5)
    atılangol = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_RadTabStrip1_goller']/span/span")

    atılangol.click()
    time.sleep(2)





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
                row = [i.text.strip( ) for i in td]

            time.sleep(3)
            next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, ") Sonraki »")))
            next_button.click()
            time.sleep(3)
        except TimeoutException:
            break
