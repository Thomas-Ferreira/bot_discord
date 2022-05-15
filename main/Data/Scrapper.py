import time
from tkinter import image_names
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import pandas as pd
from pprint import pprint

class ScrapperTest :

    def navigate (self):

        chromeOptions = webdriver.ChromeOptions()
        s = Service(r'C:/Users/thoma/OneDrive/Bureau/chrome-driver/chromedriver.exe')
        browser = webdriver.Chrome(service=s)
        siteWeb = 'https://yande.re/post?tags=genshin_impact'

        browser.get(siteWeb)
        time.sleep(3)

        ##imageNames = []
        for i in range (0,1):
            ##imageNames = browser.find_elements_by_xpath("/html/body/div[6]/div[4]/ul/li/div/a/img")
            imageNames = browser.find_elements_by_xpath("//div[@class='inner']")
            imageNames[i].click()
            time.sleep(1)
            imageSrc = browser.find_element_by_id('image').get_attribute('src')
                
        browser.close() # fermer le navigateur

        return imageSrc 

#scrapper1 = Scrapper()
#dict = scrapper1.navigate()
#pprint(dict)