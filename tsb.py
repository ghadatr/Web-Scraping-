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

# simulateur credit

def credit(wd):
    options =   Select( wd.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/section/div/div[2]/form/div/div[2]/div[2]/div/div[2]/select'))
    options.select_by_visible_text("Remboursement mensuel")
    # find element username and password for inputting login info
    montant = wd.find_element_by_xpath('//*[@id="montant_financement"]')
    apport = wd.find_element_by_xpath('//*[@id="apport_propre"]')
    revenu_mensuel = wd.find_element_by_xpath('//*[@id="revenu_mensuel_avant_impot"]')
    mensualite = wd.find_element_by_xpath('//*[@id="mensualite_autre_financement"]')
    duree = wd.find_element_by_xpath('//*[@id="duree"]')
    # Clear the fields
    apport.clear()
    revenu_mensuel.clear()
    mensualite.clear()
    duree.clear()
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  cout du projet")
    montant.send_keys(bank_montant)
    bank_apport = getpass.getpass("SVP enter Apport propre ")
    apport.send_keys(bank_apport)
    bank_revenu = getpass.getpass("SVp entrer le Revenu Mensuel Net ")
    revenu_mensuel.send_keys(bank_revenu)
    bank_mensualite = getpass.getpass("SVP enterMensualité pour d’autres Financements  ")
    mensualite.send_keys(bank_mensualite)
    bank_duree = getpass.getpass("SVp entrer le  Durée (mois) ")
    duree.send_keys(bank_duree)
    calculer = wd.find_element_by_xpath('//*[@id="calcul_simulateur"]')
    wd.execute_script("arguments[0].click();", calculer)

    time.sleep(5)
    res  = wd.find_elements_by_class_name("content-recap")
    for  b in res :
        print(b.text)




def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://www.tsb.com.tn/fr/simulateur')
    select = Select(wd.find_element_by_xpath('//*[@id="type_financement"]'))
    print("Bonjour !   ")
    print("1/Crédit Allouche (<Duree<) 	")
    print("2/Crédit Aménagement (<Duree<) 	")
    print("3/Crédit Auto Véhicule neuf 4CV (<Duree<) 	")
    print("4/Crédit Auto Véhicule neuf 9 CV et plus (<Duree<) 	")
    print("5/Crédit Auto Véhicule neuf entre 5 et 8 CV (<Duree<) 	")
    print("6/Crédit Auto Véhicule occasion 9 CV et plus (<Duree<) 	")
    print("7/crédit auto véhicule occasion entre 5 et 8CV (<Duree<) 	")
    print("8/Crédit Auto Véhicule occasion ≤ 4CV  (<Duree<) 	")
    print("9/Crédit Avenir étude à l’étranger (<Duree<) 	")
    print("10/Crédit Avenir étude en Tunisie(<Duree<) 	")
    print("11/Crédit construction	(<Duree<) ")
    print("12/Crédit Echifa	(<Duree<) ")
    print("13/Crédit Immédiat (<Duree<) 	")
    print("14/Crédit logement	(<Duree<) ")
    print("15/Crédit Mon permis de conduire (<Duree<) 	")
    print("16/Crédit Rénovation	(<Duree<) ")
    print("17/Crédit Silhouette	(<Duree<) ")
    print("18/Crédit SMARTPHONE	(<Duree<) ")
    a = int (input("Choisissez le type de financement (<Duree<) "))
    if a == 1 :
        select.select_by_index(1)
        credit(wd )
    elif a == 2 :
        select.select_by_index(2)
        credit(wd )
    elif a == 3 :
        select.select_by_index(3)
        credit(wd)
    elif a == 4 :
        select.select_by_index(4)
        credit(wd)
    elif a == 5 :
        select.select_by_index(5)
        credit(wd)
    elif a == 6 :
        select.select_by_index(6)
        credit(wd)
    elif a == 7 :
        select.select_by_index(7)
        credit(wd)
    elif a == 8 :
        select.select_by_index(8)
        credit(wd)
    elif a == 9 :
        select.select_by_index(9)
        credit(wd)
    elif a == 10 :
        select.select_by_index(10)
        credit(wd)
    elif a == 11 :
        select.select_by_index(11)
        credit(wd)
    elif a == 12 :
        select.select_by_index(12)
        credit(wd)
    elif a == 13 :
        select.select_by_index(13)
        credit(wd)
    elif a == 14 :
        select.select_by_index(14)
        credit(wd)
    elif a == 15 :
        select.select_by_index(15)
        credit(wd)
    elif a == 16 :
        select.select_by_index(16)
        credit(wd)
    elif a == 17 :
        select.select_by_index(17)
        credit(wd)
    elif a == 18 :
        select.select_by_index(18)
        credit(wd)



if __name__ == "__main__":
    main()