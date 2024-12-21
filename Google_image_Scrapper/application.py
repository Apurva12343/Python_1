from flask import Flask, render_template, request
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests

logging.basicConfig(filename='scrapper.log', level=logging.INFO, format='%(asctime)s %(message)s')

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/review", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            query = request.form['content'].replace(" ", "+")
            save_dir = 'image/'
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Set up Selenium WebDriver
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run in headless mode
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(options=options)

            # Open Google Images
            driver.get(f"https://www.google.com/search?q={query}&tbm=isch")
            time.sleep(2)

            # Scroll to load all images
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # Allow time for images to load
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                time.sleep(3)
            # Get page source and parse with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()

            # Extract image URLs
            image_tags = soup.find_all('img')
            image_data_mongo = []
            logging.info("Extracting images")

            for index, img_tag in enumerate(image_tags):
                try:
                    image_url = img_tag.get('src') or img_tag.get('data-src')
                    if image_url and image_url.startswith('http'):
                        image_data = requests.get(image_url).content
                        my_dict = {"index": index, "image": image_data}
                        image_data_mongo.append(my_dict)

                        # Save image to directory
                        with open(os.path.join(save_dir, f"{query}_{index}.jpg"), "wb") as f:
                            f.write(image_data)
                except Exception as e:
                    logging.error(f"Error downloading image {index}: {e}")

            return "Images Loaded Successfully"
        except Exception as e:
            logging.error(e)
            return "Something went wrong"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
