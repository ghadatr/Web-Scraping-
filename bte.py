import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import os
from selenium.webdriver.support.ui import Select
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit
def bankcredits(wd):
    # find element username and password for inputting login info
    montant = wd.find_element_by_name("MntCrd")
    interet = wd.find_element_by_name("TxIntf")
    periodicite = wd.find_element_by_xpath('//*[@id="Periode"]')
    select = Select(periodicite)

    annee = wd.find_element_by_xpath('//*[@id="paran"]')
    mois = wd.find_element_by_xpath('//*[@id="parmois"]')
    button = wd.find_element_by_xpath('//*[@id="myForm"]/fieldset/div[5]/div[1]/input')

# Clear the fields
    montant.clear()
    annee.clear()
    mois.clear()
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bank_montant)
    bank_interet = getpass.getpass("SVP enter Taux d'intérêt (%)* ")
    interet.send_keys(bank_interet)
    print(" 0 Mensuelle")
    print("1 Trimestrielle")
    print("2 Semestrielle")
    print("3 Quadrimestrielle")
    print("4 Bimensuelle")
    print("5 Annuelle")

    target = int(input('choisir un entier '))
    if target == 0 : select.select_by_visible_text("Mensuelle")
    elif target ==1 :select.select_by_visible_text("Trimestrielle")
    elif target == 2 :select.select_by_visible_text("Semestrielle")
    elif target == 3 :select.select_by_visible_text("Quadrimestrielle")
    elif target == 4 :select.select_by_visible_text("Bimensuelle")
    elif target == 5 :select.select_by_visible_text("Annuelle")
    annee_bank = getpass.getpass("SVP  enter Durée de remboursement  (ans) (<Duree<)  ")
    annee.send_keys(annee_bank)
    mois_bank = getpass.getpass("SVP enter Durée de remboursement restante en mois  ")
    mois.send_keys(mois_bank)

    button.click()

    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('http://www.bte.com.tn/fr/nos-simulateurs/simulateur-de-credit#')
    bankcredits(wd)
    # resultat = wd.find_element_by_name("fieldname1_2")
    tableau = wd.find_elements_by_id('tbcr')
    for el in tableau:
     print(el.text)


if __name__ == "__main__":
    main()