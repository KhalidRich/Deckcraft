from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
