from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
browser = webdriver.Chrome()

# Open the Flipkart product page
url = "https://www.linkedin.com/feed"
browser.get(url)
time.sleep(5)
email= browser.find_element(By.ID,"username")
email.send_keys("apurva.aryan@outlook.com")
password = browser.find_element(By.ID,"password")
password.send_keys("Jaiswal@2001")
time.sleep(5)
submit = browser.find_element(By.CLASS_NAME,"btn__primary--large.from__button--floating")
submit.click()
time.sleep(10)
search = browser.find_element(By.ID,"global-nav-typeahead")
search.send_keys("recruiter")
time.sleep(10)
