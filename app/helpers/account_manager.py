from app import db
from app.models import User

import bcrypt
import random
import hashlib

# Some Constants
ADMIN_USER = 0
MODERATOR_USER = 1
REGULAR_USER = 2


def create_user(form):
    salt = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    encrypted_pass = bcrypt.hashpw(str(form.password.data), salt)
    user = User(username=form.username.data,
            email=form.email.data,
            password=encrypted_pass,
            pass_salt=salt
    )
    db.session.add(user)
    db.session.commit()
    return user

def verify_user(login_form):
    username = login_form.username.data
    given_pass = login_form.username.password
    user = User.query.filter_by(username=username).first()
    if (user.password == bcrypt.hashpw(given_pass, user.salt)):
        return user
    else:
        return None

def disable_account(username):
    pass

def delete_account(username):
    pass


