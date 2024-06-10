"""NSS:Release_Versions"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class TableScraper:
    """This class represents the scraping of tables present in the url"""
    def __init__(self):
        self.driver = webdriver.Safari()
        self.final_data = []

    def open_webpage(self):
        self.driver.get("https://wiki.mozilla.org/NSS:Release_Versions")
        time.sleep(3)

    def scrape_tables(self, num_tables=3):
        """This method scraps the tables using table indexing in XPATH"""
        
        data = []
        for table_index in range(1, num_tables + 1):
            table_xpath = f'//*[@id="mw-content-text"]/table[{table_index}]'
            table = self.driver.find_element(By.XPATH, table_xpath)

            headers = [th.text.strip() for th in table.find_elements(By.XPATH, './/th')]
            #data.append(["-------------------------------------------------------------------------"])
            data.append(headers)

            for tr in table.find_elements(By.XPATH, './/tr'):
                row = [item.text.strip() for item in tr.find_elements(By.XPATH, './/td')]
                data.append(row)

        df = pd.DataFrame(data)
        df.to_csv('Link4.csv', index=False)  
        print(df)
        self.driver.quit()

table_scraper = TableScraper()
table_scraper.open_webpage()
table_scraper.scrape_tables(num_tables=3)

