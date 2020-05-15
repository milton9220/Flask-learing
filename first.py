from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    
    return render_template('index.html')


@app.route("/about")
def world():
    
    return render_template('about.html')


app.run()
