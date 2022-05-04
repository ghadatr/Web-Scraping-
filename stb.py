import selenium
import time
import getpass
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from cv2 import cv2
import os
import pytesseract
import itertools


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#rom selenium.webdriver.common.action_chains import ActionChains
path = "C:/Users/NBH/Downloads/chromedriver.exe"
driver = webdriver.Chrome(path)

#credit media
def stb_credit_media() :
    driver.get("http://www.stb.com.tn/fr/site/simulations/credit/")

    type = driver.find_element_by_id("type-credit")
    type_credit = Select(type)
    type_list = ["Crédit direct 3 ans","Crédit direct 7 ans","Crédit achat de voiture neuve 7 ans","Crédit achat de voiture d'occasion 5 ans","Crédit logement ou réaménagement 15 ans"]


    ctype = int(getpass.getpass(" enter : \n 0  pour Crédit direct 3 ans \n 1 pour Crédit direct 7 ans \n 2 pour Crédit achat de voiture neuve 7 ans \n 3 pour Crédit achat de voiture d'occasion 5 ans \n 4 pour Crédit logement ou réaménagement 15 ans"))
    type_credit.select_by_visible_text(type_list[ctype])

    slider = driver.find_element_by_xpath('//*[@id="blue-slider"]/span')

    montant = int(getpass.getpass("svp entrer le montant de credit voulu en dinars"))
    xoffset = montant/1000
    for _ in itertools.repeat(None, int(xoffset)):
        slider.send_keys(Keys.ARROW_RIGHT)


    time.sleep(1)
    #resultat = driver.find_element_by_class("remb_mensuel")
    res =driver.find_element_by_css_selector('#mensualite-credit')
    res.screenshot('C:/Users/NBH/Desktop/img.png')
    img = cv2.imread('C:/Users/NBH/Desktop/img.png')
    resultat = pytesseract.image_to_string(img)
    os.remove('C:/Users/NBH/Desktop/img.png')
    print(resultat)
    time.sleep(10)
    driver.quit()
stb_credit_media()