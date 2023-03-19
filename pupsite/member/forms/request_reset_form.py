from wtforms.validators import Email

from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField


class RequestResetForm(FlaskForm):
    """
    Form to provide functionality for requesting password reset
    """
    email = EmailField(label="Email", validators=[Email()])
    request = SubmitField(label="Reset")
