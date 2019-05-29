from bs4 import BeautifulSoup
import time
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait


driver_path = "C:\\Users\erencakir\Desktop\chromedriver.exe"

browser = webdriver.Chrome(driver_path)

klupadi = ["Akhisar",
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
           "Utaş Uşakspor", ]

for ad in klupadi:
    browser.get("http://www.tff.org/default.aspx?pageID=119")

    time.sleep(5)
    klup_adina_gore = browser.find_element_by_xpath(
        "//*[@id='ctl00_MPane_m_119_2780_ctnr_m_119_2780_RadTabStrip1_Tab3']/span/span")

    klup_adina_gore.click( )
    time.sleep(2)
    klub_adi = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_119_2780_ctnr_m_119_2780_txtKulupAdi']")
    klub_adi.send_keys(ad)
    time.sleep(2)

    # //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2"]
    ara = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_119_2780_ctnr_m_119_2780_btnSave2']")
    ara.click( )

    a = browser.page_source
    soup = BeautifulSoup(a, "lxml")
    wait = WebDriverWait(browser, 30)
    browser.execute_script("window.scrollTo(0, 800)")

    takımlar = soup.find("table", attrs={"class": "MasterTable_TFF_Contents"})
    print(takımlar)
    time.sleep(3)

