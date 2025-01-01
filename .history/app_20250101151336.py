import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "First Route!!"

@app.route("/container")
def container():
    return "container running successfully"

if __name__=="__main__":
    app.run()