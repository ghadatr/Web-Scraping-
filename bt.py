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
    montant = wd.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]/div/article/div/div[3]/span[2]/input')
    duree = wd.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]/div/article/div/div[4]/span[2]/input')
    interet = wd.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]/div/article/div/div[5]/span[2]/input')
    # Clear the fields
    montant.send_keys(Keys.CONTROL + "a")
    montant.clear()
    interet.clear()
    duree.clear()
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (DT)")
    montant.send_keys(bank_montant)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) (0<Duree<300) ")
    duree.send_keys(bank_duree)
    bank_interet = getpass.getpass("SVP enter Taux d'intérêt (%)* ")
    interet.send_keys(bank_interet)

    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('http://www.bt.com.tn/simulateur-de-credit')
    bankcredits(wd)
    # resultat = wd.find_element_by_name("fieldname1_2")
    pd = wd.find_element_by_xpath('//*[@id="montant-echeance"]')
    print("Montant de l'échéance par mois (DT):")
    print(pd.text)


if __name__ == "__main__":
    main()