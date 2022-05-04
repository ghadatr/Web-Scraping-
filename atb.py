import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import os
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit


# def Sayara(wd) :
#     sakanButton = wd.find_element_by_xpath('//*[@id="bt_sim01"]')
#     wd.execute_script("arguments[0].click();", sakanButton)
#     wd.implicitly_wait(10)
#     # find element username and password for inputting login info
#     montant = wd.find_element_by_name("txtMnt")
#     duree = wd.find_element_by_name("cmbremb")
#     duree_pre_rem = wd.find_element_by_name("txtDatdeb")
#     interet = wd.find_element_by_name("txttauCred")
#     # Clear the fields
#     montant.clear()
#     duree_pre_rem.clear()
#     interet.clear()
#     # Ask user for the information
#     wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[2]/div[2]/div[1]').click()
#     bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
#     montant.send_keys(bank_montant)
#     bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
#     duree.send_keys(bank_duree)
#     print(" 0 Mensuelle")
#     print("1 Trimestrielle")
#     print("2 Semestrielle")
#     print("3 Annuelle")
#     target = int(input('choisir un entier '))
#     if target == 0 : wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[2]/div[2]/div[1]').click()
#     elif target ==1 : wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[2]/div[2]/div[2]').click()
#     elif target == 2 : wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[2]/div[2]/div[3]').click()
#     elif target == 3 : wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[2]/div[2]/div[4]').click()
#     type_amor = getpass.getpass("SVP choisir type d'amortisement  ")
#     print("1 lineaire")
#     print("2 Annuite constante")
#     type = int(input())
#     if type == 1 : wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[3]/div[2]/div[1]').click()
#     elif type ==2 : wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[1]/div[3]/div[2]/div[2]').click()
#     bank_duree_pre = getpass.getpass("SVP enter Durée du 1er remboursement (Mois) ")
#     duree_pre_rem.send_keys(bank_duree_pre)
#     bank_interet = getpass.getpass("SVP enter interet (Mois) ")
#     interet.send_keys(bank_interet)
#     time.sleep(5)
#     wd.find_element_by_xpath('//*[@id="form_credit_sayara"]/div[2]/div/input[3]').click()
#     time.sleep(10)
#     res = wd.find_element_by_xpath('/html/body/div[4]/div[2]/div')
#     print(res.text)
#
# # wd.find_element_by_xpath("//button[@type='submit']").click()
# #     time.sleep(5)
# #     time.sleep(5)
#     return
# def Sakan(wd) :
#     sakanButton = wd.find_element_by_xpath('//*[@id="bt_sim02"]')
#     wd.execute_script("arguments[0].click();", sakanButton)
#     wd.implicitly_wait(10)
#     # wd.find_element_by_xpath('//*[@id="bt_sim02"]').click()
#     # find element username and password for inputting login info
#     montant = wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[1]/div[2]/div[1]/div[2]/input')
#     duree = wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[1]/div[2]/div[2]/div/select')
#     duree_pre_rem = wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[4]/div[2]/div[1]/div/input')
#     interet = wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[4]/div[2]/div[2]/div/input')
#
#     # Clear the fields
#     # montant.clear()
#     # duree.clear()
#     # duree_pre_rem.clear()
#     # interet.clear()
#     # Ask user for the information
#     # sakanPath = wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[2]/div[2]/div[1]')
#     # wd.execute_script("arguments[0].click();", sakanPath)
#     bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
#     montant.send_keys(bank_montant)
#     bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
#     duree.send_keys(bank_duree)
#     print(" 0 Mensuelle")
#     print("1 Trimestrielle")
#     print("2 Semestrielle")
#     print("3 Annuelle")
#     target = int(input('choisir un entier '))
#     if target == 0 : wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[2]/div[2]/div[1]').click()
#     elif target ==1 : wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[2]/div[2]/div[2]').click()
#     elif target == 2 : wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[2]/div[2]/div[3]').click()
#     elif target == 3 : wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[2]/div[2]/div[4]').click()
#     type_amor = getpass.getpass("SVP choisir type d'amortisement  ")
#     print("1 lineaire")
#     print("2 Annuite constante")
#     type = int(input())
#     if type == 1 : wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[3]/div[2]/div[1]').click()
#     elif type ==2 : wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[1]/div[3]/div[2]/div[2]').click()
#     bank_duree_pre = getpass.getpass("SVP enter Durée du 1er remboursement (Mois) ")
#     duree_pre_rem.send_keys(bank_duree_pre)
#     bank_interet = getpass.getpass("SVP enter interet (Mois) ")
#     interet.send_keys(bank_interet)
#     time.sleep(5)
#     wd.find_element_by_xpath('//*[@id="form_credit_sakan"]/div[2]/div/input[3]').click()
#     # wd.get('https://atb.tn/simulateur-credit-sayara.php/')
#     time.sleep(10)
#     res = wd.find_element_by_xpath('/html/body/div[4]/div[2]/div')
#     print(res.text)
#
#     # wd.find_element_by_xpath("//button[@type='submit']").click()
#     # time.sleep(5)
#     # time.sleep(5)
#     return
# def Direct(wd) :
#     sakanButton = wd.find_element_by_xpath('//*[@id="bt_sim03"]')
#     wd.execute_script("arguments[0].click();", sakanButton)
#     wd.implicitly_wait(10)
#     # find element username and password for inputting login info
#     montant = wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[1]/div[2]/div[1]/div[2]/input')
#     duree = wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[1]/div[2]/div[2]/div/select')
#     duree_pre_rem = wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[4]/div[2]/div[1]/div/input')
#     interet = wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[4]/div[2]/div[2]/div/input')
#     # Clear the fields
#     # montant.clear()
#     # duree_pre_rem.clear()
#     # interet.clear()
#     # Ask user for the information
#     wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[2]/div[2]/div[1]').click()
#     bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
#     montant.send_keys(bank_montant)
#     bank_duree2 = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
#     duree.send_keys(bank_duree2)
#     print(" 0 Mensuelle")
#     print("1 Trimestrielle")
#     print("2 Semestrielle")
#     print("3 Annuelle")
#     target = int(input('choisir un entier '))
#     if target == 0 : wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[2]/div[2]/div[1]').click()
#     elif target ==1 : wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[2]/div[2]/div[2]').click()
#     elif target == 2 : wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[2]/div[2]/div[3]').click()
#     elif target == 3 : wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[2]/div[2]/div[4]').click()
#     type_amor = getpass.getpass("SVP choisir type d'amortisement  ")
#     print("1 lineaire")
#     print("2 Annuite constante")
#     type = int(input())
#     if type == 1 : wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[3]/div[2]/div[1]').click()
#     elif type ==2 : wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[1]/div[3]/div[2]/div[2]').click()
#     bank_duree_pre = getpass.getpass("SVP enter Durée du 1er remboursement (Mois) ")
#     duree_pre_rem.send_keys(bank_duree_pre)
#     bank_interet = getpass.getpass("SVP enter interet (Mois) ")
#     interet.send_keys(bank_interet)
#     time.sleep(5)
#     wd.find_element_by_xpath('//*[@id="form_credit_direct"]/div[2]/div/input[3]').click()
#     # wd.get('https://atb.tn/simulateur-credit-sayara.php/')
#     time.sleep(10)
#     res = wd.find_element_by_xpath('/html/body/div[4]/div[2]/div')
#     print(res.text)
#
#     # wd.find_element_by_xpath("//button[@type='submit']").click()
#     # time.sleep(5)
#     # time.sleep(5)
#     return

def simulateur_credit_atb(wd,button_number,credit):
    sakanButton = wd.find_element_by_xpath('//*[@id="bt_sim0'+button_number+'"]')
    wd.execute_script("arguments[0].click();", sakanButton)
    wd.implicitly_wait(10)
    # find element username and password for inputting login info
    montant = wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[1]/div[2]/div[1]/div[2]/input')
    duree = wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[1]/div[2]/div[2]/div/select')
    duree_pre_rem = wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[4]/div[2]/div[1]/div/input')
    interet = wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[4]/div[2]/div[2]/div/input')
    # Clear the fields
    # montant.clear()
    # duree_pre_rem.clear()
    # interet.clear()
    # Ask user for the information
    wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[2]/div[2]/div[1]').click()
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bank_montant)
    bank_duree2 = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    duree.send_keys(bank_duree2)
    print(" 0 Mensuelle")
    print("1 Trimestrielle")
    print("2 Semestrielle")
    print("3 Annuelle")
    target = int(input('choisir un entier '))
    if target == 0 : wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[2]/div[2]/div[1]').click()
    elif target ==1 : wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[2]/div[2]/div[2]').click()
    elif target == 2 : wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[2]/div[2]/div[3]').click()
    elif target == 3 : wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[2]/div[2]/div[4]').click()
    print("SVP choisir type d'amortisement  ")
    print("1 lineaire")
    print("2 Annuite constante")
    type = int(input())
    if type == 1 : wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[3]/div[2]/div[1]').click()
    elif type ==2 : wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[1]/div[3]/div[2]/div[2]').click()
    bank_duree_pre = getpass.getpass("SVP enter Durée du 1er remboursement expl : jj/mm/aaaa ")
    duree_pre_rem.send_keys(bank_duree_pre)
    bank_interet = getpass.getpass("SVP enter interet  ")
    interet.send_keys(bank_interet)
    wd.find_element_by_xpath('//*[@id="form_credit_'+credit+'"]/div[2]/div/input[3]').click()
    time.sleep(7)
    res = wd.find_element_by_xpath('/html/body/div[4]/div[2]/div')
    print(res.text)

    # wd.find_element_by_xpath("//button[@type='submit']").click()
    # time.sleep(5)
    # time.sleep(5)
    return

def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://atb.tn/simulateur-credit/')
    time.sleep(5)


    print("Bonjour ! svp choisir un entier  ")
    print("1/Credit Sayara (1an <Duree< 7ans ) ")
    print("2/Credit Sakan (1an <Duree< 20ans )")
    print("3/Credit Direct (1an <Duree< 3ans )")
    # a = os.readline()
    a= int(input())
    if a == 1 : simulateur_credit_atb(wd,"1","sayara")
    if a == 2 : simulateur_credit_atb(wd,"2","sakan")
    elif a == 3 : simulateur_credit_atb(wd,"3","direct")

    print("Opss !! la resultat est vide ")


if __name__ == "__main__":
    main()