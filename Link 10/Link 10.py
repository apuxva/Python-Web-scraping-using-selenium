from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class WebScraper:
    """This class represents the scraping of tables present in the url"""
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.final_data = []
        self.driver.get("https://www.troemner.com/Calibration-Weights/Balance-Calibration-Weights/OIML-Calibration-Weight-Sets/c/3944")
        time.sleep(3)
        
    def scroll_to_bottom(self):
        """This method scrolls to the bottom of the page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(20)
        
    def main(self):
        """This method finds the elements on the site and appends them to a list"""
        Vendor = "Troemner"
        Product_Name = self.driver.find_element(By.TAG_NAME, 'h1').text
        time.sleep(20)
        self.data = []
        ul = self.driver.find_element(By.XPATH, '//*[@id="resultsList"]')
        for li in ul.find_elements(By.XPATH, './/li'):
            row=[]
            row.append(Vendor)
            row.append(Product_Name)
            model = li.find_element(By.TAG_NAME, 'a')
            row.append(model.text)
            description = li.find_element(By.CLASS_NAME, 'description.product-description')
            row.append(description.text)
            price = li.find_element(By.CLASS_NAME, 'priceValue')
            row.append(price.text)
            url = model.get_attribute('href')
            row.append(url)
            self.data.append(row)
        
        print(self.data)
        self.df = pd.DataFrame(self.data, columns=['Vendor','Product_Name','Model','Description',
                                    'Cost','Product_URL'])
        print(self.df)
        self.df.to_csv("Link10.csv", index=False)

# Obj & calling functions
scrapper = WebScraper()
scrapper.scroll_to_bottom()
scrapper.main()
scrapper.driver.quit()
