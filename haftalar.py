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

browser.get("http://www.tff.org/default.aspx?pageID=433")

org =["ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c1",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c2",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c3",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c4",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c5",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c6",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c7",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c8",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c9",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c10",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c11",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c12",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c13",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c14",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c15",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c16",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c17",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c18",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c19",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c20",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c21",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c22",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c23",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c24",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c25",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c26",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c27",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c28",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c29",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c30",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c31",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c32",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c33",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c34",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c35",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c36",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c37",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c38",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c39",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c40",
"ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_c41", ]

count = 0

for ad in org :
    combobox1=browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_433_2248_ctnr_m_433_2248_mOrg_combo_Image']")
    combobox1.click()

    sa = browser.find_element_by_id("%s" % ad)
    sa.click()

    hafta = ["ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c1",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c2",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c3",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c4",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c5",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c6",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c7",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c8",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c9",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c10",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c11",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c12",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c13",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c14",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c15",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c16",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c17",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c18",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c19",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c20",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c21",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c22",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c23",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c24",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c25",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c26",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c27",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c28",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c29",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c30",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c31",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c32",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c33",
             "ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_c34"
             ]
    for hf in hafta:
        time.sleep(1)
        combobox = browser.find_element_by_xpath(
            "//*[@id='ctl00_MPane_m_433_2248_ctnr_m_433_2248_h_Image']")
        combobox.click( )


        sn = browser.find_element_by_id("%s" % hf)
        sn.click()

        ara=browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_433_2248_ctnr_m_433_2248_Button1']")
        ara.click()
        wait = WebDriverWait(browser, 30)
        browser.execute_script("window.scrollTo(0, 800)")
        while True:

                a = browser.page_source
                soup = BeautifulSoup(a, "lxml")
                if soup.find("table", attrs={'class': 'GriBorder usteBG'}):
                    tablo = soup.find("table", attrs={'class': 'GriBorder usteBG'})
                    e = tablo.find("tbody")
                    table_rows = e.find_all('tr')

                    for tr in table_rows:
                        td = tr.find_all('span')
                        for span in td :
                            ere = span.find('td')
                            print(ere)

                    try:
                        browser.find_element_by_link_text(") Sonraki »").click()


                    except NoSuchElementException:
                        break


