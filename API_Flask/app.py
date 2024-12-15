from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Apurva"

@app.route('/a')
def home1():
    return "Hello, Apurva 1"


@app.route('/ap')
def home2():
    return "Hello, Apurva 2"

if __name__ == '__main__':
    app.run(host="0.0.0.0")

