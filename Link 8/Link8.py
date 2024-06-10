from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import re

class TableScraper:
    """This class represents the scraping of tables present in the url"""
    
    def __init__(self, table_xpaths, url):
        """Initialization method"""
        self.driver = webdriver.Safari()
        self.table_xpaths = table_xpaths
        self.final_data = []
        self.driver.get(url)
        time.sleep(3)

    def has_br_tag(self, element):
        """Check if the given element has a <br> tag"""
        return '<br>' in element.get_attribute('innerHTML')

    def concatenate_x_in_first_column(self, row_data):
        """Concatenate ".x" to the first column value if it doesn't contain ".x"
        and handle the special case when "and earlier" is in the first column value."""
        if row_data and row_data[0] and ".x" not in row_data[0]:
            row_data[0] = re.sub(r'\band earlier\b', '', row_data[0]).strip() + ".x"

    def EOL_Scraper(self):
        """Method to scrape tables and save data to CSV"""
        for i, table_xpath in enumerate(self.table_xpaths, start=1):
            tbody = self.driver.find_element(By.XPATH, table_xpath)
            data = []

            for tr in tbody.find_elements(By.XPATH, './/tr'):
                if self.has_br_tag(tr.find_element(By.XPATH, './/td[1]')):
                    c1_data = tr.find_element(By.XPATH, './/td[1]').get_attribute('innerHTML').split('<br>')
                    c2_data = tr.find_element(By.XPATH, './/td[2]').text.strip()
                    c3_data = tr.find_element(By.XPATH, './/td[3]').text.strip()
                    
                    for c1_element in c1_data:
                        row_data = [c1_element.strip(), c2_data, c3_data]
                        self.concatenate_x_in_first_column(row_data)
                        data.append(row_data)
                else:
                    row = [item.text.strip() for item in tr.find_elements(By.XPATH, './/td')]
                    self.concatenate_x_in_first_column(row)
                    data.append(row)

            df = pd.DataFrame(data)
            self.final_data.append(df)
            print(f"Table {i} data:\n{df}")

        final_df = pd.concat(self.final_data, ignore_index=True)
        if not final_df.empty and final_df.at[0, 0]:
            final_df.at[0, 0] = final_df.at[0, 0].replace(".x", "").strip()
        final_csv_filename = 'Link8.csv'
        final_df.to_csv(final_csv_filename, index=False)
        print(f"All tables data saved to {final_csv_filename}")
        self.driver.quit()

xpaths_example = ['//table[2]']
table_scraper = TableScraper(xpaths_example,"https://my.f5.com/manage/s/article/K5903")
table_scraper.EOL_Scraper()