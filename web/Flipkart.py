from selenium import webdriver    
from bs4 import BeautifulSoup 
import requests
 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
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
product_titles = browser.find_elements(By.CSS_SELECTOR, "div.KzDlHZ")  # CSS selector for product titles
print("List of products:")
for idx, title in enumerate(product_titles, start=1):
    print(f"{idx}. {title.text}")
time.sleep(3)
page_source = browser.page_source
flipkart_html = BeautifulSoup(page_source, 'html.parser')
bigbox = flipkart_html.findAll("div", {"class":"cPHDOP col-12-12"})
print(len(bigbox))
link = str(bigbox[2].div.div.div.a['href'])
flp = "https://www.flipkart.com"
flipkart_link = print(flp + link)
del bigbox[0:2]
for i in bigbox[:24]:
    links = i.div.div.div.a['href']
    flipkart_links = "https://www.flipkart.com"+links
time.sleep(3)
clickon = browser.find_elements(By.CLASS_NAME,"CGtC98")
for i in clickon:
    i.click()
    time.sleep(3)
    product_review = browser.find_elements(By.CLASS_NAME,"z9E0IG")
    review = browser.find_elements(By.CLASS_NAME,("ZmyHeo"))
    price = browser.find_element(By.CLASS_NAME,"hl05eU")
    name = browser.find_elements(By.XPATH,"//*[contains(@class,'_2NsDsF') and contains(@class,'AwS1CA')]")
    for i,j,k in zip(name,product_review,review):
        print(f"Customer Name {i.text}, price {price.text}, {j.text}, {k.text}")
time.sleep(3)
browser.close()
