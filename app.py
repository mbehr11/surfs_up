from flask import Flask
from flask.helpers import flash
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'