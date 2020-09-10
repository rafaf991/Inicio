from flask import Flask, render_template
import os
from flask import Flask, flash, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def a404():
    return render_template("404.html")

@app.route('/blank')
def blank():
    return render_template("blank.html")

@app.route('/buttons')
def buttons():
    return render_template("buttons.html")

@app.route('/cards')
def cards():
    return render_template("cards.html")

@app.route('/charts')
def charts():
    return render_template("charts.html")

@app.route('/forgot-password')
def forgotpassword():
    return render_template("forgot-password.html")

@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/integrals')
def integrals():
    return render_template("integrals.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/tables')
def tables():
    return render_template("tables.html")
@app.route('/utilities-animation')
def utilitiesanimation():
    return render_template("utilities-animation.html")
@app.route('/utilities-border')
def utilitiesborder():
    return render_template("utilities-border.html")
@app.route('/utilities-color')
def utilitiescolor():
    return render_template("utilities-color.html")
@app.route('/utilities-other')
def utilitiesother():
    return render_template("utilities-other.html")

if __name__ == '__main__':
    app.run(debug=True)

