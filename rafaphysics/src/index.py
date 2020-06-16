from flask import Flask, render_template
import os
from flask import Flask, flash, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/nota1')
def nota1():
    return render_template("nota1.html")

@app.route('/nota2')
def nota2():
    return render_template("nota2.html")

@app.route('/nota3')
def nota3():
    return render_template("nota3.html")

@app.route('/nota4')
def nota4():
    return render_template("nota4.html")

@app.route('/nota')
def nota():
    return render_template("nota.html")

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")

if __name__ == '__main__':
    app.run(debug=True)

