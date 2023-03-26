from wtforms.validators import EqualTo, DataRequired, Length

from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField


class ResetPasswordForm(FlaskForm):
    """
    Form to provide functionality for resetting password
    """
    password = PasswordField(
        label="New Password", validators=[DataRequired(), Length(min=6, max=40)]
    )
    verify_password = PasswordField(
        label="Verify Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords Must Match")]
    )
    reset = SubmitField(label="Reset")
