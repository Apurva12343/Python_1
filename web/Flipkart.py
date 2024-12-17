from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Creating an instance of the webdriver
browser = webdriver.Chrome()
browser.get('https://www.flipkart.com')
time.sleep(3)

# Locate the search box and search for 'iphone'
search_box = browser.find_element(By.CLASS_NAME, "Pke_EE")
search_box.send_keys("iphone")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Find all product links
product_links = browser.find_element(By.CLASS_NAME, "CGtC98")
# Iterate over each product link

    # Open the product in a new tab
product_links.send_keys(Keys.CONTROL + Keys.RETURN)
time.sleep(3)

    # Switch to the new tab
browser.switch_to.window(browser.window_handles[-1])
time.sleep(3)

try:
    # Extract product name
    product_name = browser.find_element(By.XPATH, "//*[contains(@class,'_6EBuvT')]//span").text
    print(f"Product Name: {product_name}")

    # Extract reviews, ratings, etc.
    names = browser.find_elements(By.XPATH, "//*[contains(@class,'_2NsDsF') and contains(@class,'AwS1CA')]")[0:3]
    ratings = browser.find_elements(By.XPATH, "//*[contains(@class,'XQDdHH') and contains(@class,'Ga3i8K')]")[0:3]
    product_reviews = browser.find_elements(By.CLASS_NAME, "z9E0IG")[0:3]
    reviews = browser.find_elements(By.CLASS_NAME, "ZmyHeo")[0:3]

    # Print the extracted details
    for i, j, k, l in zip(names, ratings, product_reviews, reviews):
        print(f"Name: {i.text}, Rating: {j.text}, Review: {k.text}, Review Text: {l.text}")

except Exception as e:
    print(f"Error extracting details: {e}")

    # Close the current tab
browser.close()

    # Switch back to the main tab
browser.switch_to.window(browser.window_handles[0])

# Quit the browser after processing all products
browser.quit()
