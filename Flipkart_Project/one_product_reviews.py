from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import logging
import pymongo
logging.basicConfig(filename='scrapper.log',level=logging.INFO, format='%(asctime)s %(message)s')
app = Flask(__name__)
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/review", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            searchString = request.form["content"].replace(" ", "")
            reviews_data = []
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

            # Selenium setup
            browser = webdriver.Chrome(options=options)
            browser.get("https://www.flipkart.com")
            logging.info("Flipkart Homepage")
            time.sleep(3)

            # Locate the search box and search for the product
            search_box = browser.find_element(By.CLASS_NAME, "Pke_EE")
            logging.info("Sending search String")
            search_box.send_keys(searchString)
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)

            # Find all product links
            product_links = browser.find_element(By.CLASS_NAME, "CGtC98")
            logging.info("found product links")

            # Iterate over each product link
                # Open the product in a new tab
            product_links.send_keys(Keys.CONTROL + Keys.RETURN)
            logging.info("Opeing the product in new tab")
            time.sleep(3)

            # Switch to the new tab
            browser.switch_to.window(browser.window_handles[-1])
            logging.info("going to new tab which is open")
            time.sleep(3)

            try:
                # Extract product name
                product_name = browser.find_element(By.XPATH, "//*[contains(@class,'_6EBuvT')]//span").text
                logging.info(f"Product name fetched {product_name}")

                # Extract reviews, ratings, etc.
                names = browser.find_elements(By.XPATH, "//*[contains(@class,'_2NsDsF') and contains(@class,'AwS1CA')]")[0:3]
                ratings = browser.find_elements(By.XPATH, "//*[contains(@class,'XQDdHH') and contains(@class,'Ga3i8K')]")[0:3]
                product_reviews = browser.find_elements(By.CLASS_NAME, "z9E0IG")[0:3]
                reviews = browser.find_elements(By.CLASS_NAME, "ZmyHeo")[0:3]

                # Append the extracted details to the reviews_data list
                for i, j, k, l in zip(names, ratings, product_reviews, reviews):
                    reviews_data.append({
                        "Product": product_name,
                        "Name": i.text,
                        "Rating": j.text,
                        "CommentHead": k.text,
                        "Comment": l.text
                    })
                try:
                       client = pymongo.MongoClient("mongodb+srv://iamapurvaaryan:Apurva@cluster0.lzgwt20.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Connect to MongoDB (adjust URI as needed)
                       db = client["one_product_flipkart_reviews"]  # Database name
                       collection = db["reviews"]
                       collection.insert_many(reviews_data)
                except Exception as e:
                    logging.error("error in mongodb")
            except Exception as e:
                logging.error(f"Error extracting details: {e}")

                # Close the current tab
            logging.info("closing the current tab")
            browser.close()

                # Switch back to the main tab
            logging.info("going back to to the products tab")
            browser.switch_to.window(browser.window_handles[0])

            # Quit the browser
            browser.quit()

            return render_template("result.html", reviews=reviews_data)

        except Exception as e:
            logging.error(f"Error: {e}")
            return "Something went wrong. Please try again."

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
