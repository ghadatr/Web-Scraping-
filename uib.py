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
def bankcredits(wd, i, credits):
    credit = wd.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[3]/div/div[2]/div/div/h3['+i+']/a')
    wd.execute_script("arguments[0].click();", credit)
    wd.implicitly_wait(10)
    wd.get('https://www.uib.com.tn/index.php/'+credits+'?view=application')

# find element username and password for inputting login info
    revenu = wd.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input')
    montant = wd.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input')
    duree = wd.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[3]/form/table/tbody/tr[5]/td[2]/select')
    # Clear the fields
    montant.clear()
    revenu.clear()
    # Ask user for the information
    bank_interet = getpass.getpass("SVP enter le Revenu mensuel (en DT)")
    revenu.send_keys(bank_interet)

    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (Dt)")
    montant.send_keys(bank_montant)

    bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
    duree.send_keys(bank_duree)
    wd.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[3]/form/table/tbody/tr[8]/td/input[1]').click()
    res = wd.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[3]/form/table/tbody/tr[7]/td')
    print("la resultat est :")

    print(res.text)

    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)

    wd.get('https://www.uib.com.tn/simulateur-de-credit/simulateur/simulateur-de-credit#faqnoanchor')
    time.sleep(5)
    print("1 Expresso  ")
    print("2 AMENAGEMENT ET TRAVAUX  ")
    print("3 MAHLY  ")
    print("4 RAPID'MAHLY  ")
    print("5 DARI  ")
    print("6 OMNIA  ")
    print("7 AUTO ")
    a = int(input("choisir un choix" ))
    if a==1 :
        bankcredits(wd,"1","simulateur-expresso/simulateur-expresso")
    elif a == 2:
     bankcredits(wd, "2","simulateur-amenagement")
    elif a == 3:
     bankcredits(wd, "3", "simulateur-mahly/simulateur-mahly")
    elif a == 4:
        bankcredits(wd, "4", "simulateur-rapidmahly/simulateur-rapidmahly")
    elif a == 5:
        bankcredits(wd, "5", "simulateur-dari")
    elif a == 6:
        bankcredits(wd, "6", "simulateur-omnia")
    elif a == 7:
        bankcredits(wd, "7", "simulateur-auto")
    # resultat = wd.find_element_by_name("fieldname1_2")




if __name__ == "__main__":
    main()