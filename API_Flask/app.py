from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Apurva"

@app.route("/test")
def test():
    a = 5+6
    return "this is my function to run app {}".format(a)

@app.route("/test2")
def test2():
    data = request.args.get("x")
    return "this is the data input from my url {}".format(data)

@app.route('/a')
def home1():
    return "Hello, Apurva 1"


@app.route('/ap')
def home2():
    return "Hello, Apurva 2"

if __name__ == '__main__':
    app.run(host="0.0.0.0")

