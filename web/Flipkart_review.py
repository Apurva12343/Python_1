from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
browser = webdriver.Chrome()

# Open the Flipkart product page
url = "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4"
browser.get(url)

try:
    # Close the login popup if it appears
    try:
        close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button._2KpZ6l._2doB4z"))
        )
        close_button.click()
    except:
        print("No popup appeared.")

    # Scroll to ensure the element is visible
    browser.execute_script("window.scrollTo(0, 300);")

    # Locate the product name
    product_name_element = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h1/span"))
    )
    product_name = product_name_element.text
    name = browser.find_elements(By.XPATH,"//*[contains(@class,'_2NsDsF') and contains(@class,'AwS1CA')]")[0:3]
    rating = browser.find_elements(By.XPATH,"//*[contains(@class,'XQDdHH') and contains(@class,'Ga3i8K')]")[0:3]
    product_review = browser.find_elements(By.CLASS_NAME,"z9E0IG")[0:3]
    review = browser.find_elements(By.CLASS_NAME,("ZmyHeo"))[0:3]
    name1 = browser.find_element(By.XPATH,"//h1/span")
    print(f"{name1.text}")
    for i,j,k,l in zip(name,rating,product_review,review):
        print(f"{product_name},{i.text},{j.text},{k.text},{l.text}")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    browser.quit()
