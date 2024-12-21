from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("https://www.youtube.com/@PW-Foundation/streams")
time.sleep(5)
thumb = browser.find_elements(By.ID,"video-title-link")
print(len(thumb))