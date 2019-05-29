import mysql.connector
from selenium import webdriver
from bs4 import BeautifulSoup
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
    kartlar = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_RadTabStrip1_kartlar']/span/span")

    kartlar.click()
    time.sleep(2)
    yil = ["ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c1",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c2",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c3",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c4",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c5",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c6",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c7",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c8",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c9",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c10",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c11",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c12",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c13",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c14",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c15",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c16",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c17",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c18",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c19",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c20",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c21",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c22",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c23",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c24",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c25",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c26",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c27",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c28",
           "ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_c29"]
    for yıl in yil:
        combobox = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_SezonSelector4_combo_Image']")
        combobox.click( )
        time.sleep(3)

        sn = browser.find_element_by_id("%s" % yıl)
        sn.click()



        wait = WebDriverWait(browser, 30)
        browser.execute_script("window.scrollTo(0, 800)")
        while True:
            try:
                a = browser.page_source
                soup = BeautifulSoup(a, "lxml")
                if soup.find("table", attrs={'class': 'MasterTable_TFF_Contents'}):
                    tablo = soup.find("table", attrs={'class': 'MasterTable_TFF_Contents'})
                    e = tablo.find("tbody")
                    table_rows = e.find_all('tr')

                    for tr in table_rows:
                        td = tr.find_all('td')
                        row = [i.text.strip() for i in td]
                        #print(row)
                        kartlargif=[]
                        gifs=[]
                        maclink = []
                        links = []
                        for gif in tr.findAll('img'):
                            gifs.append(gif.get('src'))
                        kartlargif.append(gifs[0])
                        print(kartlargif)
                        #browser.get("http://www.tff.org/%s"%kartlargif)
                        for link in tr.findAll('a'):
                            links.append(link.get('href'))
                        maclink.append(links[0])
                        #print(maclink)
                    time.sleep(3)
                    next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, ") Sonraki »")))
                    next_button.click()
            except TimeoutException:
                break