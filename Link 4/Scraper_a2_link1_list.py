from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class ListScraper:
    def __init__ (self):
        self.driver = webdriver.Safari()
        self.list_data=[]   
    def open_webpage (self):
        self.driver.get("https://wiki.mozilla.org/NSS:Release_Versions")
    
    def list_scraper (self):
        list_element = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/ul[1]')
        list_items = list_element.find_elements(By.XPATH, './/li')
        self.list_data = [item.text for item in list_items]
        print(self.list_data)
        df= pd.DataFrame(self.list_data)
        df.to_csv('list_l1_data.csv', index= False)
        print(df)
    def close_browser(self):
        self.driver.quit()
        
obj = ListScraper()
obj.open_webpage()
obj.list_scraper()
obj.close_browser()
        
        