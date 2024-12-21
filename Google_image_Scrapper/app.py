from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import pymongo
import os
import logging
logging.basicConfig(filename='scrapper.log',level=logging.INFO, format='%(asctime)s %(message)s')
app = Flask(__name__)
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")
@app.route("/review", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            query = request.form['content'].replace(" ","")
            save_dir = ('image/')
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
            response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")
            logging.info("Got response")
            soup = BeautifulSoup(response.content,'html.parser')
            image_tags = soup.find_all('img')
            del image_tags[0]
            image_data_mongo = []
            logging.info("going in for loop")
            for i in  image_tags:
                image_url = i['src']
                image_data = requests.get(image_url).content
                my_dict = {"index":index,"image":image_data}
                image_data_mongo.append(my_dict)
                with open(os.path.join(save_dir,f"{query}_{image_tags.index(i)}.jpg"),"wb") as f:
                    f.write(image_data)
            return "Image Loaded"
        except Exception as e:
            logging.info(e)
            return "something is wrong"
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)