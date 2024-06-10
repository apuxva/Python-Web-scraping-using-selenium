"""Operating sytem,End of support,License model"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class TableScraper:
    """This class represents the scraping of tables present in the url"""
    def __init__ (self):
        self.driver = webdriver.Safari()
        self.driver.get("https://cloud.ibm.com/docs/vpc?topic=vpc-guest-os-lifecycle&_gl=1*yli673*_ga*NzQ2NzU4NjE5LjE2Nzc3NTIwOTI.*_ga_FYECCCS21D*MTY5MDQ3MDE4NS4yMi4xLjE2OTA0NzA2MzcuMC4wLjA")
        time.sleep(3)
        
    def scrape_tables(self):
        """scraps all the present tables on the url"""
        tables = self.driver.find_elements(By.XPATH, '//table')
        data = []
        
        for table in tables:
            headers = [th.text.strip() for th in table.find_elements(By.XPATH, './/th')]
            #data.append(["-------------------------------------------------------------------------"])
            data.append(headers)
            
            for tr in table.find_elements(By.XPATH, './/tr'):
                row = [item.text.strip() for item in tr.find_elements(By.XPATH, './/td')]
                data.append(row)
                
        df = pd.DataFrame(data)
        df.to_csv('Link5.csv', index=False)  
        print(df)
        self.driver.quit()

table_scraper = TableScraper()
scraped_data = table_scraper.scrape_tables()
