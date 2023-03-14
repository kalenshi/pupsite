from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField, PasswordField
from wtforms.validators import Email, EqualTo, Length


class MemberForm(FlaskForm):
    """
    Form for creating New members on the pup site
    """
    first_name = StringField(label="Name", validators=[Length(min=2, max=50)])
    last_name = StringField(label="Name", validators=[Length(min=2, max=50)])
    email = EmailField(label="Email", validators=[Email()])
    verify_email = EmailField(label="Verify Email", validators=[EqualTo("email", "The emails must Match")])
    password = PasswordField(label="Password")
    verify_password = PasswordField(label="Verify Password", validators=[EqualTo("password")])
    submit = SubmitField(label="Add Owner")
