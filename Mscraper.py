from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class WebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.gehealthcare.com/products/ultrasound/ultrasound-digital-solutions")
        self.accept_cookies()
        self.cards = []

    def accept_cookies(self):
        time.sleep(1)
        accept_button = self.driver.find_element(By.XPATH, '//*[@id="_evidon-accept-button"]')
        accept_button.click()
        print("Clicked on the Accept All button for cookies.")

    def main(self):
        Vendor = "GE HealthCare"
        time.sleep(2)
        self.data = []

        ul = self.driver.find_element(By.TAG_NAME, 'ul')
        product = ul.find_element(By.XPATH, '//*[@id="primary-navigation-item-0"]')
        product.click()
        time.sleep(2)
        
        sub_menu = self.driver.find_element(By.ID, 'sub-menu-container')
        left_div = sub_menu.find_element(By.ID, 'secondTierMenuLink_0')
        ultrasound = left_div.find_element(By.XPATH, '//*[@id="secondTierMenuLink_0"]/div[2]')
        ultrasound.click()
        time.sleep(2)
        right_div = sub_menu.find_element(By.CLASS_NAME, 'menu-content-container-center-right')
        anchor_tag = right_div.find_element(By.XPATH, '//*[@id="menu-content-wrapper"]/div/div/div/div[2]/div/div[1]/div/div[2]/a[1]')

        # Get the href attribute value
        href_value = anchor_tag.get_attribute("href")
        time.sleep(2)
        # Redirect to the href link
        self.driver.get(href_value)
        
        main_div = self.driver.find_element(By.XPATH, '//*[@id="sub-specialty"]/div/div[2]/div[2]/div[1]')

        name_divs = main_div.find_elements(By.XPATH, './/div[@class="mdc-layout-grid__inner"]')
        Product_name = [nested_div.text for i, nested_div in enumerate(name_divs) if i % 2 == 0]

        anchor_divs = main_div.find_elements(By.XPATH, './/p[@class="sub-specialty-cta-text ptags-small"]/a')
        Product_URL = [a_tag.get_attribute("href") for a_tag in anchor_divs]
        
        for name, url in zip(Product_name, Product_URL):
            self.cards.append({'Vendor': Vendor, 'Product_name': name, 'Product_URL': url})

        self.df = pd.DataFrame(self.cards, columns=['Vendor', 'Product_name', 'Product_URL'])
        self.df.to_csv("Link11.csv", index=False)

    def close_browser(self):
        self.driver.quit()
scraper = WebScraper()
scraper.main()
scraper.close_browser()