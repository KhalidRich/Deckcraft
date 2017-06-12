from app import db
from app.models import User

import bcrypt
import random
import hashlib
import uuid

# Some Constants
DUMMY_USER = -1
ADMIN_USER = 0
MODERATOR_USER = 1
REGULAR_USER = 2


def create_user(form):
    salt = uuid.uuid4().hex
    hashword = hashlib.sha512(form.password.data + salt).hexdigest()
    user = User(username=form.username.data,
            email=form.email.data,
            password=hashword,
            pass_salt=salt
    )
    db.session.add(user)
    db.session.commit()
    return user

def verify_user(login_form):
    username = login_form.username.data
    given_pass = login_form.username.password
    user = User.query.filter_by(username=username).first()
    if (user.password == hashlib.sha512(given_pass + user.salt).hexdigest()):
        return user
    else:
        return None

def disable_account(username):
    pass

def delete_account(username):
    pass

def get_default_user():
    return User.query.filter_by(_id=0).first()
