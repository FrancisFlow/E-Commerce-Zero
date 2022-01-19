from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def  index():
   return render_template ('index.html')

@app.route('/about')
def about():
   return render_template ('about.html')

@app.route('/contact')
def contact():
   return render_template ('contact.html')


@app.route('/cart')
def cart():
   return render_template ('cart.html')

@app.route('/men')
def women():
   return render_template ('men.html')

@app.route('/women')
def men():
   return render_template ('women.html')

@app.route('/login')
def login():
   return render_template ('login.html')

@app.route('/signup')
def signup():
   return render_template ('signup.html')