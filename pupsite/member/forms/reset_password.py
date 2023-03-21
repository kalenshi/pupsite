from wtforms.validators import EqualTo, DataRequired

from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField


class ResetPasswordForm(FlaskForm):
    """
    Form to provide functionality for resetting password
    """
    password = PasswordField(label="New Password", validators=[DataRequired()])
    verify_password = PasswordField(
        label="Verify Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords Must Match")]
    )
    reset = SubmitField(label="Reset")
