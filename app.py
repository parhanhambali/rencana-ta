from distutils.log import debug
from re import template
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def indexku():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)