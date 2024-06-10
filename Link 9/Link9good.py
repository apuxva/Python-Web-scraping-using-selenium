from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class WebScraper:
    def __init__(self, url):
        """
        Initializes the WebScraper class.

        Parameters:
        - url (str): The URL of the webpage to scrape.
        """
        self.url = url
        self.driver = webdriver.Chrome()
        self.h4_list = []
        self.id_list = []

    def load_page(self):
        """
        Loads the webpage specified by the URL.
        """
        self.driver.get(self.url)
        time.sleep(5)

    def scrape_data(self):
        """
        Scrapes data from the webpage, including 'h4' tags and elements with the text "ID".
        """
        h4_tags = self.driver.find_elements(By.TAG_NAME, 'h4')[:9]
        for h4_tag in h4_tags:
            self.h4_list.append(h4_tag.text)

        elements_with_id = self.driver.find_elements(By.XPATH, '//*[contains(text(), "ID")]')[:9]
        for element in elements_with_id:
            self.id_list.append(element.text)

    def create_dataframe(self):
        """
        Creates a DataFrame from the scraped data and saves it to a CSV file.
        """
        df = pd.DataFrame({'Model': self.h4_list, 'Model ID': self.id_list})
        df.to_csv('Link99.csv', index=False)

    def close_browser(self):
        """
        Closes the web browser.
        """
        self.driver.quit()

def main():
    """
    Main function to instantiate the WebScraper class, perform scraping, and clean up.
    """
    url = 'https://www.ricoh-usa.com/en/products/pl/discontinued'
    scraper = WebScraper(url)

    scraper.load_page()
    scraper.scrape_data()
    scraper.create_dataframe()
    scraper.close_browser()

if __name__ == "__main__":
    main()