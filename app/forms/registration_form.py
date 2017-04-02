from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Re-type password')
    accept_tos = BooleanField('I accept the terms and conditions of Deckcraft.', [DataRequired()])

