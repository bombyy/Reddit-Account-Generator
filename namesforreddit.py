from cgitb import text
from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import re
import string
import secrets
import os
import mail
import json
import urllib.request

dirname = os.path.dirname(__file__)

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

if connected:
    while True:
        driver = webdriver.Chrome(ChromeDriverManager().install()) # USES CHROMEDRIVERMANAGER TO AUTO UPDATE CHROMEDRIVER
        # GENERATE PASSWORD
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(16))
        # PASSWORD GENERATION FINISHED
        # NAME GENERATION
        driver.get('https://en.wikipedia.org/wiki/Special:Random')
        temp = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "firstHeading"))).text
        for char in string.punctuation:
            temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
        for char in string.digits:
            temp = temp.replace(char, '') #REMOVES SPACES
        temp = "".join(filter(lambda char: char in string.printable, temp)) #REMOVES NON ASCII CHARACTERS
        name = ''.join(temp.split())
        name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


        randomNumber = random.randint(10000,99999)

        username = name+str(randomNumber)
        password = password
        email = mail.email_address()
        print(username, email, password)
        # NAME GENERATION FINISHED
        time.sleep(4)
        # REDDIT ACCOUNT CREATION
        driver.get('https://www.reddit.com/register/')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'regEmail'))).send_keys(email)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'regUsername'))).send_keys(username)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'regPassword'))).send_keys(password)

        with open("accounts.txt", "a") as f:
            user_str = "\n"+str({
                "username":username,
                "password":password
            }) + ","
            f.write(user_str)
            f.close()

        with open("account_email.txt", "a") as f:
            user_str = "\n"+str({
                "username":username,
                "password":password,
                "email":email
            }) + ","
            f.write(user_str)
            f.close()

        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div[3]/button"))).click()

        print("\n\n"+f"Check for verification mail here: https://www.guerrillamail.com/\nUse address: {email.replace('@guerrillamailblock.com', '')}")
        driver.close()
        inp=print(input("WAIT UNTIL YOUR VPN HAS CHANGED LOCATION!\nCreate another account? (Enter) Or Close (type 'q' + Enter)"))
        if inp == "q":
            exit()
