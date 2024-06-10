from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class WebScraping:
    """This class scrapes the details of the product"""
    def __init__(self):
        """Webdriver, url, data list"""
        self.driver = webdriver.Chrome()
        self.url = 'https://us.vwr.com/store/product/8017133/troemner-alloy-8-precision-analytical-weight-sets-class-2-troemner'
        self.driver.get(self.url)
        time.sleep(10)

    def extract_table_data(self):
        """Extracts the table headings and contents"""
        table = self.driver.find_element(By.XPATH, '//*[@id="order"]')
        header_data = [th.text for th in table.find_elements(By.XPATH, './/th')[:7]]

        # Extract only odd rows (excluding the header)
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
        table_data = [header_data] + [[td.text for td in row.find_elements(By.XPATH, './/td')[:7]] for i, row in enumerate(rows) if i % 2 == 0]

        self.driver.quit()
        self.save_to_csv(table_data)

    def save_to_csv(self, table_data):
        df = pd.DataFrame(table_data)
        csv_filename = 'Link6.csv'
        df.to_csv(csv_filename, index=False)
        print(f'Table data has been successfully saved to {csv_filename}')

obj = WebScraping()
obj.extract_table_data()
