from wtforms.validators import Email, DataRequired

from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField


class RequestResetForm(FlaskForm):
    """
    Form to provide functionality for requesting password reset
    """
    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    request = SubmitField(label="Reset")
