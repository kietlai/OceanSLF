from flask import Flask, render_template, redirect, url_for, flash

app = Flask('app')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-us')
def about():
    return render_template('aboutme.html')

@app.route('/citations')
def mla():
    return render_template('mla.html')

@app.route('/solutions')
def solution():
    return render_template('solution.html')

@app.route('/problem')
def problem():
    return render_template('problem.html')


if __name__ == '__main__':
    app.run(debug=True)