from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass
from cv2 import cv2
import os
import pytesseract
from pynput.keyboard import Key, Controller

# simulateur credit
def credit(wd , i ):
    wd.get("https://www.ubci.tn/particuliers/outils-et-guides/"+i)
    wd.find_element_by_xpath('//*[@id="cookiewarning"]/div/div[2]/div/input').click()
    montant =wd.find_element_by_xpath('//*[@id="montant"]')
    wd.execute_script("arguments[0].click();", montant)
    duree=wd.find_element_by_xpath('//*[@id="duree"]')
    wd.execute_script("arguments[0].click();", duree)
    if i  in {'credit-perso-auto/?simu=1#simulateur' ,"credit-immobilier/?simu=1#simulateur","credit-immobilier/?simu=2#simulateur" ,"credit-immobilier/?simu=3#simulateur","credit-perso-auto/?simu=2#simulateur"}:
        taux= wd.find_element_by_xpath('//*[@id="taux"]')
        taux.send_keys(Keys.CONTROL + "a")
        taux_ubci = getpass.getpass("entrer le taux nominal <15 ")
        taux.send_keys(taux_ubci)
    # # find element username and password for inputting login info
    # Clear the fields
    montant.clear()
    duree.send_keys(Keys.CONTROL + "a")
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité  inferieur a 15000 TND(FCFA)")
    montant.send_keys(bank_montant)
    duree.send_keys(Keys.CONTROL + "a")
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (mois) ")
    duree.send_keys(bank_duree)


    wd.find_element_by_xpath('//*[@id="simulation"]').click()
    res =wd.find_elements_by_css_selector('#thesimu > div > div > div.col-xs-12.col-sm-5.col-sm-height.simulateur.bggry2.gray > div')
    for i in res :
        print(i.text)
    return

    # time.sleep(5)
    # time.sleep(5)
    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    print("Bonjour !   ")
    print("1/crédit Conso Distribution ")
    print ("2/ Credit Perso")
    print ("3/ Credit Auto")
    print("4/crédit Immobilier 	")
    print (" 4.1 ) Residence principale")
    print (" 4.2 ) Residence secondaire")
    print (" 4.3) Terrain")

    a = float (input("choisir un type de credit "))
    time.sleep(5)
    if a == 1 :
        credit(wd, "credit-conso/?simu=1#simulateur")
    if a == 2 :
        credit(wd, "credit-perso-auto/?simu=1#simulateur")
    if a == 3 :
        credit(wd, "credit-perso-auto/?simu=2#simulateur")
    if a == 4.1 :
        credit(wd, "credit-immobilier/?simu=1#simulateur")
    if a == 4.2 :
        credit(wd , "credit-immobilier/?simu=2#simulateur")
    if a == 4.3 :
        credit(wd, "credit-immobilier/?simu=3#simulateur")


if __name__ == "__main__":
    main()