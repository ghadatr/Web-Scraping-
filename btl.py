import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import getpass
from cv2 import cv2
import os
import pytesseract
import re
from pynput.keyboard import Key, Controller

# simulateur credit
def bankcredits(wd, ):
    # find element username and password for inputting login info
    Total_Prix_Acquisition= wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/div/main/article/div/div/div/div/div/div/article/form/div[2]/div/input')
    Apport_Propre = wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/div/main/article/div/div/div/div/div/div/article/form/div[3]/div/input')
    Revenu_Mensuel_Brut= wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/div/main/article/div/div/div/div/div/div/article/form/div[4]/div/input')
    duree = wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/div/main/article/div/div/div/div/div/div/article/form/div[5]/div/select')
    # Clear the fields
    Total_Prix_Acquisition.clear()
    Apport_Propre.clear()
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer Total Prix Acquisition (DT) *")
    Total_Prix_Acquisition.send_keys(bank_montant)
    bank_interet = getpass.getpass("SVP enter Apport Propre (DT) ")
    Apport_Propre.send_keys(bank_interet)
    bank_duree = getpass.getpass("SVP enter Revenu Mensuel Brut (DT) *                                 ")
    Revenu_Mensuel_Brut.send_keys(bank_duree)
    bank_duree = getpass.getpass("SVP enter Duree (ans) *                       ")
    duree.send_keys(bank_duree)
    wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/div/main/article/div/div/div/div/div/div/article/form/div[6]/input').click()
    time.sleep(5)
    res = wd.find_elements_by_css_selector('#full-screen-search > div > div.simulateur-result-content')

    for i in  res :
        print(i.text)





def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://www.btl.tn/simulateur')
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/div/main/article/div/div/div/div/div/div/article/form/div[1]/div/select'))
    print("Bonjour !   ")
    print("1/Crédit consommation")
    print("2/ Crédit voiture neuve ( 5 CV et plus)  (1 < Duree < 7 ) ")
    print("3/Crédit voiture occasion")
    print("4/Crédit immobilier")
    print("5/Crédit voiture neuve ( 4 CV )")
    a = int (input("choisir un type de credit "))
    if a == 1 :
        select.select_by_visible_text("Crédit consommation")
        bankcredits(wd)
    elif a == 2 :
        select.select_by_visible_text("Crédit voiture neuve ( 5 CV et plus)")
        bankcredits(wd)
    elif a == 3 :
        select.select_by_visible_text("Crédit voiture occasion")
        bankcredits(wd)
    elif a == 4 :
        select.select_by_visible_text("Crédit immobilier")
        bankcredits(wd)
    elif a == 5 :
        select.select_by_visible_text("Crédit voiture neuve ( 4 CV )")
        bankcredits(wd)





if __name__ == "__main__":
    main()