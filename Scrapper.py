import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import pandas as pd
from pprint import pprint

class Scrapper :

    def navigate (self):

        chromeOptions = webdriver.ChromeOptions()
        s = Service(r'C:/Users/thoma/OneDrive/Bureau/chrome-driver/chromedriver.exe')
        browser = webdriver.Chrome(service=s)
        siteWeb = 'https://yande.re/post?tags=genshin_impact'

        browser.get(siteWeb)
        time.sleep(3)

        imageLinks = browser.find_elements_by_xpath("//a//img")
        imageNames = []
        for element in range (0,1):
            imageNames.add(element.get_attribute("src"))
        
        dictionary = {"Url": imageNames}
        browser.close() # fermer le navigateur

        return dictionary 

scrapper1 = Scrapper()
dict = scrapper1.navigate()
pprint(dict)