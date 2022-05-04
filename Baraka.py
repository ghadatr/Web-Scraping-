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
    Options= Select(wd.find_element_by_xpath('//*[@id="type_financement"]'))

    # find element username and password for inputting login info
    montant = wd.find_element_by_name("montant_financement")
    Apport_Propre= wd.find_element_by_name("apport_propre")
    Revenu_Mensuel_Net= wd.find_element_by_name("revenu_mensuel_avant_impot")
    duree= wd.find_element_by_name("duree")
    Mensualité_pour_Financements= wd.find_element_by_name("mensualite_autre_financement")
    # Clear the fields
    montant.clear()
    Apport_Propre.clear()
    Revenu_Mensuel_Net.clear()
    Mensualité_pour_Financements.clear()
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bank_montant)
    bank_Apport_Propre = getpass.getpass("SVP enter Apport Propre                                         ")
    Apport_Propre.send_keys(bank_Apport_Propre)
    bank_Revenu_Mensuel_Net = getpass.getpass("SVP enterRevenu Mensuel Net avant impôt                                              ")
    Revenu_Mensuel_Net.send_keys(bank_Revenu_Mensuel_Net)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    duree.send_keys(bank_duree)
    bank_Mensualité_pour_Financements = getpass.getpass("SVP enter Mensualité pour d’autres Financements ")
    Mensualité_pour_Financements.send_keys(bank_Mensualité_pour_Financements)
    wd.find_element_by_xpath('//*[@id="calcul_simulateur"]').click()
    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://www.albarakabank.com.tn/fr/simulateur/')
    select = Select(wd.find_element_by_xpath('//*[@id="type_financement"]'))
    time.sleep(5)
    print("Bonjour !   ")
    print("1/Dar Al Baraka")
    print("2/ DAR ALBARAKA PREMIER LOGEMENT")
    print("3/Dirasset Al Baraka")
    print("4/Omra Al Baraka")
    print("5/Premier Logement Al Baraka")
    print("6/Rafehat Al Baraka ")
    print("7/Rahalet Al Baraka ")
    print("8/Sayarat Al Baraka Neuve 4CH ")
    print("9/Sayarat Al Baraka Neuve 5-8CH ")
    print("10/Sayarat Al Baraka neuve 9CH + ")
    print("11/Sayarat Al Baraka Occasion 4 CH")
    print("12/Sayarat Al Baraka Occasion 5-8 CH ")
    print("13/Sayarat Al Baraka Occasion 9CH + ")
    print("14/Tahsin Masken Al Baraka ")
    print("15/Tahsin Masken Plus Al Baraka ")
    a = int (input("choisir un type de credit "))
    if a == 1 :
        select.select_by_index(1)
        bankcredits(wd)
    elif a == 2 :
         select.select_by_index(2)
         bankcredits(wd)
    elif a == 3 :
         select.select_by_index(3)
         bankcredits(wd)
    elif a == 4 :
         select.select_by_index(4)
         bankcredits(wd)
    elif a == 5 :
         select.select_by_index(5)
         bankcredits(wd)
    elif a == 6 :
         select.select_by_index(6)
         bankcredits(wd)
    elif a == 7 :
         select.select_by_index(7)
         bankcredits(wd)
    elif a == 8 :
         select.select_by_index(8)
         bankcredits(wd)
    elif a == 9 :
         select.select_by_index(9)
         bankcredits(wd)
    elif a == 10 :
         select.select_by_index(10)
         bankcredits(wd)
    elif a == 11 :
         select.select_by_index(11)
         bankcredits(wd)
    elif a == 12 :
         select.select_by_index(12)
         bankcredits(wd)
    elif a == 13 :
         select.select_by_index(13)
         bankcredits(wd)
    elif a == 14:
         select.select_by_index(14)
         bankcredits(wd)
    elif a == 15:
         select.select_by_index(15)
         bankcredits(wd)



    time.sleep(5)
    pd = wd.find_element_by_xpath('//*[@id="box-recap"]/div/div')
    print("la resultat est :")
    print(pd.text)


if __name__ == "__main__":
    main()