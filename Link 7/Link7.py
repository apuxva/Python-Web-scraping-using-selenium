"""Version and Dates"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

class WebScraper:
    """This class represents the scraping of tables present in the url"""
    def __init__(self):
        """This method has the
        __init__ method"""
        self.driver = webdriver.Safari()

    def main(self):
        """This method fetches the Version and Dates in the url"""
        self.driver.get("https://winscp.net/eng/docs/history#google_vignette")

        h2_tags = self.driver.find_elements(By.TAG_NAME, 'h2')
        time_tags = self.driver.find_elements(By.TAG_NAME, 'time')  

        data = []
        for h2, time_tag in zip(h2_tags, time_tags):
            h2_text = h2.text
            time_text = time_tag.text
            data.append([h2_text, time_text])
       
        df = pd.DataFrame(data, columns=['Version', 'Date'])
        df.to_csv('Link7.csv', index=False)
        print(df)
        print(f'Data has been saved')
        self.driver.quit()


scraper = WebScraper()
scraper.main()


