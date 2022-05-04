import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import os
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit
def bankcredits(wd):
    # find element username and password for inputting login info
    montant = wd.find_element_by_name("fieldname8_2")
    interet = wd.find_element_by_name("fieldname9_2")
    duree = wd.find_element_by_name("fieldname10_2")
# Clear the fields
    montant.clear()
    interet.clear()
    duree.clear()
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bank_montant)
    bank_interet = getpass.getpass("SVP enter Taux d'intérêt (%)* ")
    interet.send_keys(bank_interet)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
    duree.send_keys(bank_duree)

    time.sleep(5)
    # wd.find_element_by_xpath("//button[@type='submit']").click()
    # time.sleep(5)
    # time.sleep(5)
    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://www.banqueatlantique.net/simulateur-de-credit/')
    time.sleep(5)
    bankcredits(wd)
    # resultat = wd.find_element_by_name("fieldname1_2")
    wd.find_elements_by_xpath('//*[@id="fieldname1_2"]')
    pd = wd.find_element_by_id("fieldname1_2")
    print("la resultat est :")
    print(pd.text)
    print("Opss !! la resultat est vide ")


if __name__ == "__main__":
    main()