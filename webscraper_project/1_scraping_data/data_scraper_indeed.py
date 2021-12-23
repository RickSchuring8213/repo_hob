import pandas as pd
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('webscraper_project/1_scraping_data/chromedriver')
print('Ok')
driver.get('https://www.google.nl')