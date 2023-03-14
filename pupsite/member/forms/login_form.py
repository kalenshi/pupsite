from wtforms.validators import Email

from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField


class LoginForm(FlaskForm):
    """
    Form to provide functionality for user login
    """
    email = EmailField(label="Email", validators=[Email()])
    password = PasswordField(label="Password")
    login = SubmitField(label="Login")
