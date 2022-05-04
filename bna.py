import selenium
import time
from cv2 import cv2
import os
import pytesseract
import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = 'C:/Users/NBH/Downloads/chromedriver.exe'
driver = webdriver.Chrome(path)

#credit direct
def bna_direct_financement() :
    driver.get("http://www.bna.tn/site/fr/simulateur.php?id_article=587#horizontalTab1")
    type = driver.find_element_by_id("produit")
    type_credit = Select(type)
    type_list = ["Crédits Directs aux Particuliers et aux Professionnels","PRET AUTO- Crédit Direct Acquisition véhicule","PRET PERSO- Crédit Direct Dépenses Courantes","PRET IMMO - Crédit Direct Aménagement Logement Hypothécaire","PRET PERSO - Crédit Direct Aménagement","PRET IMMO- Crédit Direct Acquisition Logement","PRET IMMO- Crédit Direct Construction","PRET IMMO- Crédit Direct Achat Terrain","PRET PERSO - Crédit Direct Aménagement Hypothécaire"]

    ctype = int(getpass.getpass("enter le type de credit voulu : \n 0 " +type_list[0]+"  \n 1 pour "+type_list[0]+ "\n 2 pour " +type_list[0]+"  \n 3 pour "+type_list[3]+ "\n 4 " +type_list[4]+"  \n 5 pour "+type_list[5]+ "\n 6 pour " +type_list[6]+"  \n 7 pour "+type_list[7] + "\n 8 pour " +type_list[8]))
    type_credit.select_by_visible_text(type_list[ctype])



    montant = driver.find_element_by_xpath('//*[@id="montant"]')
    montant.clear()
    b_montant = getpass.getpass(" enter le montant de credit voulu en dinars ")
    montant.send_keys(b_montant)


    type_r = driver.find_element_by_id("periodicite")
    type_remboursement = Select(type_r)
    type_r_list = ["Mensuelle","Trimestrielle","Semestrielle","Annuelle"]
    ctyper = getpass.getpass(" enter la Périodicité de remboursement voulu : \n 0  pour Mensuelle \n 1 pour Trimestrielle \n 2 pour Semestrielle \n 3 pour Annuelle ")
    type_remboursement.select_by_visible_text(type_r_list[int(ctyper)])

    remboursement = driver.find_element_by_xpath('//*[@id="slider_duree"]/span')
    dure = int(getpass.getpass("svp entrer la durée de credit voulu en mois qui ne depasse pas 300"))
    for _ in itertools.repeat(None, int(dure - 1)):
        remboursement.send_keys(Keys.ARROW_RIGHT)

    type_remboursement = driver.find_element_by_xpath('//*[@id="date_echeance"]')
    type_remboursement.clear()
    tr = getpass.getpass("entrer la date de debut de remboursement sous la forme de jj-mm-aaaa")
    type_remboursement.send_keys(tr)


    calculer = driver.find_element_by_id("envoyer")
    calculer.click()
    time.sleep(1)

    res = driver.find_element_by_xpath('//*[@id="horizontalTab"]/div/div[1]/div/div[2]/div/b[2]')
    print(res.text)


def bna_direct_remboursement() :
    driver.get("http://www.bna.tn/site/fr/simulateur.php?id_article=587#horizontalTab2")
    type =Select( driver.find_element_by_xpath('//*[@id="produit2"]'))
    type_list = ["Crédits Directs aux Particuliers et aux Professionnels","PRET AUTO- Crédit Direct Acquisition véhicule","PRET PERSO- Crédit Direct Dépenses Courantes","PRET IMMO - Crédit Direct Aménagement Logement Hypothécaire","PRET PERSO - Crédit Direct Aménagement","PRET IMMO- Crédit Direct Acquisition Logement","PRET IMMO- Crédit Direct Construction","PRET IMMO- Crédit Direct Achat Terrain","PRET PERSO - Crédit Direct Aménagement Hypothécaire"]
    for index in range (0,  (len(type_list)-1)):
        print("choisir un  Catégorie" )
        print  ( index.__str__() + ") "+ type_list[index]  )
    a   = int(input())
    type.select_by_index(a+1)



    montant = driver.find_element_by_xpath('//*[@id="salaire"]')
    montant.clear()
    b_montant = getpass.getpass(" enter votre salaire en dinars ")
    montant.send_keys(b_montant)

    retenue = driver.find_element_by_xpath('//*[@id="retenue"]')
    retenue.clear()
    b_retenue = getpass.getpass(" enter le retenue en dinars ")
    retenue.send_keys(b_retenue)

    remboursement = driver.find_element_by_xpath('//*[@id="slider_duree2"]/span')
    dure = int(getpass.getpass("svp entrer la durée de credit voulu en mois qui ne depasse pas 240"))
    for _ in itertools.repeat(None, int(dure - 1)):
        remboursement.send_keys(Keys.ARROW_RIGHT)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodicite"]')))
    type_remboursement = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/div/div[1]/div[1]/div/div/div[2]/form/div[2]/div[3]/div/select'))


    # type_r = driver.find_element_by_xpath('//*[@id="periodicite"]')
    type_r_list = ["Mensuelle","Trimestrielle","Semestrielle","Annuelle"]
    for index in range (0,  (len(type_r_list))):
        print("choisir un  Catégorie" )
        print  ( index.__str__() + ") "+ type_r_list[index]  )
    a   = int(input())
    type_remboursement.select_by_visible_text(type_r_list[a])

    type_remboursement = driver.find_element_by_id("date_echeance2")
    type_remboursement.clear()
    tr = getpass.getpass("entrer la date de debut de remboursement sous la forme de jj-mm-aaaa")
    type_remboursement.send_keys(tr)


    calculer = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/div/div[1]/div[1]/div/div/div[2]/form/input')
    driver.execute_script("arguments[0].click();", calculer)

    time.sleep(5)

    res = driver.find_elements_by_css_selector('#horizontalTab > div > div.smart-forms.resp-tab-content.resp-tab-content-active > div > div.pricetable-holder > div')
    for i in res :
        print(i.text)

bna_direct_remboursement()