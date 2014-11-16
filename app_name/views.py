from flask import render_template
from app_name import app


@app.route('/')
def home():
    return render_template('home.html')


# error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
