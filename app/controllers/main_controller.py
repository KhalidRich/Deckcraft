from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db

import time

@app.route('/')
def index():
    user = None #TODO: Make proper logic to set the user using g.user
    if user is None:
        return render_template('landing_page.html')
    return render_template('index.html', current_user=user)
