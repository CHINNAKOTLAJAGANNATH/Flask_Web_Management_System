from flask import Blueprint, render_template, request, flash, redirect, url_for

index = Blueprint('index', __name__)

@index.route('/')
def flask():
    return render_template('index/flask.html')

@index.route('/home')
def home():
    return render_template('index/home.html')

@index.route('/about')
def about():
    return render_template('index/about.html')