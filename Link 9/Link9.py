"""Web-Scraping to find Discontinued Printers and copiers using regex"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re

class WebScraping:
    """this class is used for web-scraping"""
    
    def __init__(self):
        """webdriver, url, and data lists"""
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ricoh-usa.com/en/products/pl/discontinued")
        self.data_list = []
        self.filtered_list = []

    def main(self):
        """This method scraps the model number and model id of the product"""
        
        element = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[5]/div')
        element_text = element.text
        self.data_list = [element_text]

        # using regex for model number and model ID
        model_number_pattern = r'\b(PJ\s\w+)\b'
        model_id_pattern = r'\b(ID:\s\d+)\b'

        model_number_matches = re.findall(model_number_pattern, element_text)
        model_id_matches = re.findall(model_id_pattern, element_text)

        # Creating a DataFrame
        df = pd.DataFrame({'Model Number': model_number_matches, 'Model ID': model_id_matches})
        df.to_csv("Link9.csv", index=False)
        self.driver.quit()

# Example usage:
obj = WebScraping()
obj.main()
