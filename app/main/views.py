from flask import render_template, redirect, url_for
from . import main


@main.route('/')
def index():

    """
    view root page function
    """

    title = "ShoeHub"
    return render_template('index.html', title = title)