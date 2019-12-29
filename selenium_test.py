from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("./chromedriver")


paragraph =[]
driver.get("https://www.bloomberg.com/news/articles/2019-12-18/tesla-considers-cutting-price-of-china-built-cars-next-year")

content = driver.page_source
soup = BeautifulSoup(content)
for p in soup.findAll('p'):
    paragraph.append(p)

print(paragraph)
