from flask import Blueprint, render_template, request
#from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return render_template('index.html')