from selenium import webdriver    
from bs4 import BeautifulSoup 
import requests
from lxml import html
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
 
# Creating an instance webdriver
browser = webdriver.Chrome()
browser.get('https://www.flipkart.com')
time.sleep(3)
search_box = browser.find_element(By.CLASS_NAME, "Pke_EE")  # Locate the search box
search_box.send_keys("iphone")  # Example: Search for 'laptop'
search_box.send_keys(Keys.RETURN)
time.sleep(3)
clickon = browser.find_elements(By.CLASS_NAME,"CGtC98")
for i in clickon:
    i.click()
    time.sleep(5)
    product_name = browser.find_elements(By.XPATH,"//*[contains(@class,'cPHDOP') and contains(@class,'col-12-12')]")[2].text[26:60]
    name = browser.find_elements(By.XPATH,"//*[contains(@class,'_2NsDsF') and contains(@class,'AwS1CA')]")[0:3]
    rating = browser.find_elements(By.XPATH,"//*[contains(@class,'XQDdHH') and contains(@class,'Ga3i8K')]")[0:3]
    product_review = browser.find_elements(By.CLASS_NAME,"z9E0IG")[0:3]
    review = browser.find_elements(By.CLASS_NAME,("ZmyHeo"))[0:3]
    for i,j,k,l in zip(name,rating,product_review,review):
        print(f"{product_name},{i.text},{j.text},{k.text},{l.text}")
browser.quit()
