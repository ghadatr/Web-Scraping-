import urllib

import selenium
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from cv2 import cv2
import os
import pytesseract
from bs4 import BeautifulSoup as bs
import os
from selenium.webdriver.support.ui import Select
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit
def creditImmo(wd):
    # find element username and password for inputting login info
    data = wd.find_elements_by_xpath('//*[@id="tabs-1"]/form/div[3]/div')
    for i in data :
        print(i.text)
    time.sleep(5)
    print(" 0 Tamouil Menzel")
    print("1 Tamouil Binaet")
    print("2 Tamouil Akkarat El Afrad")
    print("3 Tamouil Tahsinet")
    print("4 Tamouil Tahsinet +")
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[2]/div/select'))
    target = int(input('choisir un type de Financement'))
    if target == 0 : select.select_by_visible_text("Tamouil Menzel")
    elif target ==1 :select.select_by_visible_text("Tamouil Binaet")
    elif target == 2 :select.select_by_visible_text("Tamouil Akkarat El Afrad")
    elif target == 3 :select.select_by_visible_text("Tamouil Tahsinet")
    elif target == 4 :select.select_by_visible_text("Tamouil Tahsinet +")
    Total_Prix_Acquisition = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[6]/div/input')
    Apport_Propre= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[7]/div/input')
    Revenu_brut = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/input')
    Mensualité_Autres_Financements= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/input')
    Durée_de_Remboursement= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[3]/div[1]/input')
    # Clear the fields
    Durée_de_Remboursement.send_keys(Keys.CONTROL + "a")
    # Ask user for the information
    bank_TOTAL = getpass.getpass("SVp entrer leTotal Prix Acquisition *:")
    Total_Prix_Acquisition.send_keys(bank_TOTAL)
    bank_APPORT = getpass.getpass("SVp entrer le Apport Propre :")
    Apport_Propre.send_keys(bank_APPORT)
    bank_REVENU = getpass.getpass("SVp entrer le Revenu brut *:")
    Revenu_brut.send_keys(bank_REVENU)
    bank_AUTRE = getpass.getpass("SVP enter Mensualité Autres Financements                             ")
    Mensualité_Autres_Financements.send_keys(bank_AUTRE)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    Durée_de_Remboursement.send_keys(bank_duree)

    submit =wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[2]/div/div/input[7]').click()
    wd.execute_script("arguments[0].click();", submit)
    time.sleep(10)
    res = wd.find_elements_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[5]/div/div[2]/div[1]/div')

    for i in  res :
        print(i.text)

def creditAuto(wd):
    # find element username and password for inputting login info
    data = wd.find_elements_by_xpath('//*[@id="tabs-1"]/form/div[3]/div')
    for i in data :
        print(i.text)
    time.sleep(5)
    print(" 0 Tamouil Sayara - Voiture")
    print("1 Tamouil Sayara - Bateau")
    print("2 Tamouil Sayara - Moto")
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div/select'))
    target = int(input('choisir un type de Financement'))
    if target == 0 : select.select_by_visible_text("Tamouil Sayara - Voiture")
    elif target ==1 :select.select_by_visible_text("Tamouil Sayara - Bateau")
    elif target == 2 :select.select_by_visible_text("Tamouil Sayara - Moto")
    print(" 0/ 4CV")
    print("1/ 5CV+")
    print("2/ 9CV+")
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[2]/div/select'))
    target = int(input('choisir le puissance fiscale :'))
    if target == 0 : select.select_by_visible_text("4 CV")
    elif target ==1 :select.select_by_visible_text("5 CV +")
    elif target == 2 :select.select_by_visible_text("9 CV +")
    print(" 0/ Neuf")
    print("1/ Occasion")
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[3]/div/select'))
    target = int(input('choisir le Type de véhicule *:'))
    if target == 0 : select.select_by_visible_text("Neuf")
    elif target ==1 :select.select_by_visible_text("Occasion")

    Total_Prix_Acquisition = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[6]/div/input')
    Apport_Propre= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[7]/div/input')
    Revenu_brut = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/input')
    Mensualité_Autres_Financements= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/input')
    Durée_de_Remboursement= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[3]/div[1]/input')
    # Clear the fields
    Durée_de_Remboursement.send_keys(Keys.CONTROL + "a")
    # Ask user for the information
    bank_TOTAL = getpass.getpass("SVp entrer leTotal Prix Acquisition *:")
    Total_Prix_Acquisition.send_keys(bank_TOTAL)
    bank_APPORT = getpass.getpass("SVp entrer le Apport Propre :")
    Apport_Propre.send_keys(bank_APPORT)
    bank_REVENU = getpass.getpass("SVp entrer le Revenu brut *:")
    Revenu_brut.send_keys(bank_REVENU)
    bank_AUTRE = getpass.getpass("SVP enter Mensualité Autres Financements                             ")
    Mensualité_Autres_Financements.send_keys(bank_AUTRE)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    Durée_de_Remboursement.send_keys(bank_duree)

    wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[2]/div/div/input[7]').click()
    time.sleep(10)
    res = wd.find_elements_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[5]/div/div[2]/div[1]/div')


    for i in  res :
        print(i.text)

def creditVoyage(wd) :
    # find element username and password for inputting login info
    data = wd.find_elements_by_xpath('//*[@id="tabs-1"]/form/div[3]/div')
    for i in data :
        print(i.text)
    time.sleep(5)
    print(" 0 Tamouil Omra")
    print("1 Tamouil Rahalet")
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[2]/div/select'))
    target = int(input('choisir un type de Financement'))
    if target == 0 :
        select.select_by_visible_text("Tamouil Omra")
        nbre_pers = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[5]/div/input')
        nbre_pers.send_keys(Keys.CONTROL + "a")
        bank_pers = getpass.getpass("SVp entrer nombre de personne")
        nbre_pers.send_keys(bank_pers)
    elif target == 1 :select.select_by_visible_text("Tamouil Rahalet")

    Total_Prix_Acquisition = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[6]/div/input')
    Apport_Propre= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[7]/div/input')
    Revenu_brut = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/input')
    Mensualité_Autres_Financements= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/input')
    Durée_de_Remboursement= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[3]/div[1]/input')
    # Clear the fields
    Durée_de_Remboursement.send_keys(Keys.CONTROL + "a")
    # Ask user for the information

    bank_TOTAL = getpass.getpass("SVp entrer leTotal Prix Acquisition *:")
    Total_Prix_Acquisition.send_keys(bank_TOTAL)
    bank_APPORT = getpass.getpass("SVp entrer le Apport Propre :")
    Apport_Propre.send_keys(bank_APPORT)
    bank_REVENU = getpass.getpass("SVp entrer le Revenu brut *:")
    Revenu_brut.send_keys(bank_REVENU)
    bank_AUTRE = getpass.getpass("SVP enter Mensualité Autres Financements                             ")
    Mensualité_Autres_Financements.send_keys(bank_AUTRE)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    Durée_de_Remboursement.send_keys(bank_duree)

    wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[2]/div/div/input[7]').click()
    # wd.execute_script("arguments[0].click();", submit)
    time.sleep(10)
    res = wd.find_elements_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[5]/div/div[2]/div[1]/div')

    for i in  res :
        print(i.text)
def creditAutre(wd) :
    # find element username and password for inputting login info
    data = wd.find_elements_by_xpath('//*[@id="tabs-1"]/form/div[3]/div')
    for i in data :
        print(i.text)
    print("0/ Tamouil Mochtarayet")
    print("1/ Tamouil Dirasset")
    print("2/ Tamouil Khadamet Sehheya")
    select = Select(wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[2]/div/select'))
    target = int(input('choisir un type de Financement'))
    if target == 0 : select.select_by_visible_text("Tamouil Mochtarayet")
    elif target ==1 :select.select_by_visible_text("Tamouil Dirasset")
    elif target == 2 :select.select_by_visible_text("Tamouil Khadamet Sehheya")


    Total_Prix_Acquisition = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[6]/div/input')
    Apport_Propre= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[1]/div[7]/div/input')
    Revenu_brut = wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/input')
    Mensualité_Autres_Financements= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/input')
    Durée_de_Remboursement= wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[1]/div/div[2]/div[3]/div[1]/input')
    # Clear the fields
    Durée_de_Remboursement.send_keys(Keys.CONTROL + "a")
    Revenu_brut.send_keys(Keys.CONTROL + "a")
    Mensualité_Autres_Financements.send_keys(Keys.CONTROL + "a")
    # Ask user for the information
    bank_TOTAL = getpass.getpass("SVp entrer leTotal Prix Acquisition *:")
    Total_Prix_Acquisition.send_keys(bank_TOTAL)
    bank_APPORT = getpass.getpass("SVp entrer le Apport Propre :")
    Apport_Propre.send_keys(bank_APPORT)
    bank_REVENU = getpass.getpass("SVp entrer le Revenu brut *:")
    Revenu_brut.send_keys(bank_REVENU)
    bank_AUTRE = getpass.getpass("SVP enter Mensualité Autres Financements")
    Mensualité_Autres_Financements.send_keys(bank_AUTRE)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    Durée_de_Remboursement.send_keys(bank_duree)

    wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[4]/div/div/div/div[2]/div/div/input[7]').click()
    time.sleep(10)
    res = wd.find_elements_by_class_name("results")
    for i in  res :
        print(i.text)
    return


def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://www.banquezitouna.com/fr/simulateur')
    time.sleep(5)
    print("Bonjour ! svp choisir un entier  ")
    print("1/Financement Immobilier  ")
    print("2/Financement Véhicule  ")
    print("3/Financement Voyage  ")
    print("4/ Financement Autres Achats  ")
    a = int(input())
    if a==1 :
        wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[2]/div/div/div[1]/div/div[1]/div/label').click()
        creditImmo(wd)
    elif a==2:
        wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[2]/div/div/div[1]/div/div[2]/div/label').click()
        creditAuto(wd)
    elif a==3:
        wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[2]/div/div/div[1]/div/div[3]/div/label').click()
        creditVoyage(wd)

    elif a==4 :
        wd.find_element_by_xpath('/html/body/div[1]/main/div[5]/div/div/div/div/div[1]/div/div[1]/form/div[2]/div/div/div[1]/div/div[4]/div/label').click()
        creditAutre(wd)




if __name__ == "__main__":
    main()