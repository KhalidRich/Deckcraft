from app import db
import bcrypt

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    pass_salt = db.Column(db.String(512), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=1)
