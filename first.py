from flask import Flask, escape, request

app = Flask(__name__)

@app.route("/")
def hello():
    
    return "Hello Milton bhai "


@app.route("/milton")
def world():
    
    return "Hello Milton bai 2"


app.run()
