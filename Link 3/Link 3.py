from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class TableScraper:
    """This class represents the scraping of tables present in the url"""
    
    def __init__(self, table_xpaths):
        """This method has the
        __init__ method 
        :param table_xpath: xpath of the tables needed to be scraped"""
        self.driver = webdriver.Safari()
        self.table_xpaths = table_xpaths
        self.final_data = []

    def open_webpage(self, url):
        """this method fetches the url of the site"""
        self.driver.get(url)
        time.sleep(3)

    def EOL_Scraper(self):
        """This method takes the x_path of tables and gets the data of the headings and the tr and td tags of the table"""
        for i, table_xpath in enumerate(self.table_xpaths, start=1):
            tbody = self.driver.find_element(By.XPATH, table_xpath)
            headers = [th.text.strip() for th in tbody.find_elements(By.XPATH, './/th')]
            data = []
            for tr in tbody.find_elements(By.XPATH, './/tr'):
                row = [item.text.strip() for item in tr.find_elements(By.XPATH, './/td')]
                data.append(row)
            df = pd.DataFrame(data, columns=headers)
            self.final_data.append(df)
            print(f"Table {i} data:\n{df}")

        final_df = pd.concat(self.final_data, ignore_index=True)
        final_csv_filename = 'Link3.csv'
        final_df.to_csv(final_csv_filename, index=False)
        print(f"All tables data saved to {final_csv_filename}")
        self.driver.quit()

xpaths_example = ['//*[@id="section_2"]/table']
table_scraper = TableScraper(xpaths_example)
table_scraper.open_webpage("https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates")
table_scraper.EOL_Scraper()