from app import db

# Some constants
ADMIN_ROLE = 0
MODERATOR_ROLE = 1
USER_ROLE = 2

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
