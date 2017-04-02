from app import db
import bcrypt

# Some constants
ADMIN_ROLE = 0
MODERATOR_ROLE = 1
USER_ROLE = 2

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    pass_salt = db.Column(db.String(512), nullable=False)

    def create_user(registration_form):
        salt = bcrypt.gensalt()
        encrypted_pass = bcrypt.hashpw(form.password.data, salt)
        user = User.new(username=form.username.data,
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

