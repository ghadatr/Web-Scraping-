
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import getpass
from cv2 import cv2
import os

# simulateur credit

def creditBH(wd, i):
    wd.get('https://bh.com.tn/'+i)
    # find element username and password for inputting login info

    montant = wd.find_element_by_xpath('//*[@id="montant"]')
    age = wd.find_element_by_xpath('//*[@id="age_client"]')
    revenue = wd.find_element_by_xpath('//*[@id="revenue"]')
    engagement= wd.find_element_by_xpath('//*[@id="engagement_mensuels"]')
    duree = wd.find_element_by_xpath('//*[@id="duree"]')
        # Clear the fields
    # Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bank_montant)
    select = Select(wd.find_element_by_xpath('//*[@id="categorie"]'))
    print(" 0 Profession libérale")
    print("1 Salarié")
    print("2 Seniors")
    print("3 Tunisien résident à l'étranger")

    target = int(input('choisir un entier '))
    if target == 0 : select.select_by_visible_text("Profession libérale")
    elif target ==1 :select.select_by_visible_text("Salarié")
    elif target == 2 :select.select_by_visible_text("Seniors")
    elif target == 3 :select.select_by_visible_text("Tunisien résident à l'étranger")

    print(" 1 Mensuels")
    print("2 Annuels")
    a= int(input())
    if a == 1 :
        mem = wd.find_element_by_xpath('/html/body/div[2]/div[8]/div/div[1]/div[2]/div/form/div[3]/div/div[1]/input[1]')
        wd.execute_script("arguments[0].click();", mem)

    elif a == 2 :
         annu=   wd.find_element_by_xpath('/html/body/div[2]/div[8]/div/div[1]/div[2]/div/form/div[3]/div/div[1]/input[2]')
         wd.execute_script("arguments[0].click();", annu)
    revenu_client=getpass.getpass("entrer le revenu selon votre choix")
    revenue.send_keys(revenu_client)
    if i == "crédit-voiture" :
        typeVoiture = Select(wd.find_element_by_xpath('//*[@id="type_voiture"]'))
        d = ["Neuve puissance 4 chevaux","Neuve puissance > 4 chevaux","Occasion puissance 4 chevaux","Occasion puissance > 4 chevaux"]
        for index in range (0,  (len(d))):
                print("choisir un  Catégorie" )
                print  (    index.__str__() + ") "+ d[index]  )
        a = int(input())
        typeVoiture.select_by_index(a+1)

    age_client =getpass.getpass("entre l'age ")
    age.send_keys(age_client)

    engagement_bank = getpass.getpass('SVp entrer Autre engagement mensuels)')
    engagement.send_keys(engagement_bank)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    duree.send_keys(bank_duree)

    wd.find_element_by_xpath('//*[@id="btn_simulation"]').click()
    time.sleep(7)
    res =wd.find_elements_by_css_selector('#details > div.col-md-12.cadre_sim')

    for i in  res :
        print(i.text)

    # time.sleep(5)
    return


def creditHabitat(wd) :
        wd.get("https://bh.com.tn/crédit-habitat")

        montant = wd.find_element_by_xpath('//*[@id="montant"]')
        age = wd.find_element_by_xpath('//*[@id="age_client"]')
        revenue = wd.find_element_by_xpath('//*[@id="revenue"]')
        engagement= wd.find_element_by_xpath('//*[@id="engagement_mensuels"]')
        duree = wd.find_element_by_xpath('//*[@id="duree"]')
        # Clear the fields
        # Ask user for the information
        bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
        montant.send_keys(bank_montant)
        select = Select(wd.find_element_by_xpath('//*[@id="categorie"]'))
        print(" 0 Profession libérale")
        print("1 Salarié")
        print("2 Seniors")
        print("3 Tunisien résident à l'étranger")

        target = int(input('choisir un entier '))
        if target == 0 : select.select_by_visible_text("Profession libérale")
        elif target ==1 :select.select_by_visible_text("Salarié")
        elif target == 2 :select.select_by_visible_text("Seniors")
        elif target == 3 :select.select_by_visible_text("Tunisien résident à l'étranger")

        print(" 1 Mensuels")
        print("2 Annuels")
        a= int(input())
        if a == 1 :
            mem = wd.find_element_by_xpath('/html/body/div[2]/div[8]/div/div[1]/div[2]/div/form/div[3]/div/div[1]/input[1]')
            wd.execute_script("arguments[0].click();", mem)

        elif a == 2 :
            annu=   wd.find_element_by_xpath('/html/body/div[2]/div[8]/div/div[1]/div[2]/div/form/div[3]/div/div[1]/input[2]')
            wd.execute_script("arguments[0].click();", annu)
        revenu_client=getpass.getpass("entrer le revenu ")
        revenue.send_keys(revenu_client)

        print("Crédit Normal - Lié à l'épargne logement ?")
        print(" 1 oui")
        print("2 non")
        a= int(input())
        if a == 2 :
            mem = wd.find_element_by_xpath('/html/body/div/div[8]/div/div[1]/div[2]/div/form/div[4]/div/div/input[1]')
            wd.execute_script("arguments[0].click();", mem)

        elif a == 1 :
            annu=   wd.find_element_by_xpath('/html/body/div/div[8]/div/div[1]/div[2]/div/form/div[4]/div/div/input[2]')
            wd.execute_script("arguments[0].click();", annu)
            choix = Select(wd.find_element_by_xpath('//*[@id="categorie_normal"]'))
            d= ["G - 6an(s)","G - 5an(s)","G - 4an(s)","H - 6an(s)","H - 4an(s)","H - 5an(s)","I - 6an(s)","I - 4an(s)","I - 5an(s)","J - 6an(s)","J - 4an(s)","J - 5an(s)","K - 6an(s)","K - 5an(s)","K - 4an(s)","L - 4an(s)","L - 5an(s)","L - 6an(s)","M - 5an(s)","M - 6an(s)","M - 4an(s)","N - 5an(s)","N - 6an(s)","N - 4an(s)","P - 5an(s)","P - 6an(s)","P - 4an(s)"]
            for index in range (0,  (len(d)-1)):
                print("choisir un  Catégorie" )
                print  ( index.__str__() + ") "+ d[index]  )
            a = int(input())
            choix.select_by_index(a+1)


        print("Crédit Jedid - lié à l'épargne Jedid ?")
        print(" 1 oui")
        print("2 non")
        a= int(input())
        if a == 2 :
            mem = wd.find_element_by_xpath('/html/body/div/div[8]/div/div[1]/div[2]/div/form/div[7]/div/div/input[1]')
            wd.execute_script("arguments[0].click();", mem)

        elif a == 1 :
            annu=   wd.find_element_by_xpath('/html/body/div/div[8]/div/div[1]/div[2]/div/form/div[7]/div/div/input[2]')
            wd.execute_script("arguments[0].click();", annu)
            choix = Select(wd.find_element_by_xpath('//*[@id="categorie_jedid"]'))
            d= ["A - 1an(s)","A - 4an(s)","A - 2an(s)","A - 3an(s)","B - 2an(s)","B - 3an(s)","B - 1an(s)","B - 4an(s)","C - 2an(s)","C - 3an(s)","C - 1an(s)","C - 4an(s)","D - 1an(s)","D - 4an(s)","D - 2an(s)","D - 3an(s)","E - 2an(s)","E - 3an(s)","E - 1an(s)","E - 4an(s)","F - 1an(s)","F - 4an(s)","F - 2an(s)","F - 3an(s)"]
            for index in range (0,  (len(d))):
                print("choisir un  Catégorie" )
                print  ( index.__str__() + ") "+ d[index]  )
            a = int(input())
            choix.select_by_index(a+1)

        age_client =getpass.getpass("entre l'age ")
        age.send_keys(age_client)

        engagement_bank = getpass.getpass('SVp entrer Autre engagement mensuels)')
        engagement.send_keys(engagement_bank)
        bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) (entre 1ans et 25ans ) ")
        duree.send_keys(bank_duree)

        wd.find_element_by_xpath('/html/body/div[2]/div[8]/div/div[1]/div[2]/div/form/div[15]/div/button[1]').click()
        time.sleep(10)
        res = wd.find_elements_by_css_selector('#details3 > div.col-md-12.cadre_sim')
        for i in  res :
            print(i.text)
        return


def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    # pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    print("Bonjour !   ")
    print("1/crédit aménagement (1ans<Duree<7ans) 	")
    print("2/crédit à la consommation (1ans<Duree<3ans) 	")
    print("3/crédit d'habitat (1ans <Duree< 25ans)  	")
    print("4/crédit voiture (1ans<Duree<7ans) 	")
    a = int (input("choisir un type de credit "))
    time.sleep(5)
    if a == 1 :
        creditBH(wd, "crédit-aménagement")
    if a == 2 :
        creditBH(wd, "crédit-consommation")
    if a == 3 :
        creditHabitat(wd)
    if a == 4 :
        creditBH(wd, "crédit-voiture")



if __name__ == "__main__":
    main()