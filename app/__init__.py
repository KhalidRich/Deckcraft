import os
from config import basedir, DATABASE_URI
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import controllers
from app import models
from app import forms
