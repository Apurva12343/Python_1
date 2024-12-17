from selenium import webdriver    
from bs4 import BeautifulSoup 
import requests
 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.google.com')
time.sleep(3)
search_box = browser.find_element(By.CLASS_NAME,"gLFyf")
search_box.send_keys("Crunchbase")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
clickon = browser.find_element(By.LINK_TEXT,"News")
clickon.click()
time.sleep(3)
news = browser.find_elements(By.CLASS_NAME,"SoAPf")
file = open("news.txt","w")
for i in news:
    file.write(i.text)