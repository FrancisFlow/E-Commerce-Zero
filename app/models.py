from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/about')
def about():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('about.html')

# categories
@app.route('/women')
def  women():
    return render_template('women.html')


@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/boys')
def boys():
    return render_template('boys.html')


@app.route('/girls')
def girls():
    return render_template('girls.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')










