"""Scraper - Link 1
https://learn.microsoft.com/en-us/surface/surface-driver-firmware-lifecycle-support"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class TableScraper:
    """This class scraps the tables with Manual xpaths and manual url input"""
    
    def __init__(self, table_xpaths):
        self.driver = webdriver.Safari()
        self.table_xpaths = table_xpaths
        self.final_data = []

    def open_webpage(self, url):
        self.driver.get(url)
        time.sleep(3)

    def scrape_tables(self):
        """This method gives the headings to each and every table"""
        data=[]
        for i, table_xpath in enumerate(self.table_xpaths, start=1):
            tbody = self.driver.find_element(By.XPATH, table_xpath)
            headers = [th.text.strip() for th in tbody.find_elements(By.XPATH, './/th')]
            #data.append(["-------------------------------------------------------------------------"])
            data.append(headers)  # Append th tags first

            for tr in tbody.find_elements(By.XPATH, './/tr'):
                row = [item.text.strip() for item in tr.find_elements(By.XPATH, './/td')]
                data.append(row) #then append the contents

            df = pd.DataFrame(data)
            self.final_data.append(df)
            print(f"Table {i} data:\n{df}")

        final_df = pd.concat(self.final_data, ignore_index=True)
        final_csv_filename = 'Link1.csv'
        final_df.to_csv(final_csv_filename, index=False)
        print(f"All tables data saved to {final_csv_filename}")
        self.driver.quit()

xpaths_example = ['//*[@id="main"]/div[3]/div[8]/table', '//*[@id="main"]/div[3]/div[11]/table']
table_scraper = TableScraper(xpaths_example)
table_scraper.open_webpage("https://learn.microsoft.com/en-us/surface/surface-driver-firmware-lifecycle-support")
table_scraper.scrape_tables()
