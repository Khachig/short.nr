from flask import Flask

app = Flask(__file__)


@app.route('/')
def home():
    return 'Hello World'
