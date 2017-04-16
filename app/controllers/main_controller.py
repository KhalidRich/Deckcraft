from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from app.forms import *
from app.models import User
from app.helpers import account_manager

import time

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Home page
@app.route('/')
def index():
    user = None #TODO: Make proper logic to set the user using g.user
    if user is None:
        return render_template('landing_page.html')
    return render_template('index.html', current_user=user)

# Registration, Login, and Logout Logic
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    registration_form = RegistrationForm()
    if request.method == 'GET':
        return render_template('signup.html', form=registration_form)
    elif request.method == 'POST':
        user = account_manager.create_user(registration_form)
        flash('Account created! Now let\'s get to building.')
        return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'GET':
        print(render_template('login.html', form=login_form))
        return render_template('login.html', form=login_form)
    elif request.method == 'POST' and login_form.validate():
        flash('Log in successful. Now let\'s get to building.')
        return redirect('/')

@app.route('/logout')
def logout():
    if request.method == 'GET':
        pass
