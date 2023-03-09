from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField
from wtforms.validators import Email, EqualTo, Length


class MemberForm(FlaskForm):
    """
    Form for creating New members on the pup site
    """
    name = StringField(label="Name", validators=[Length(min=2, max=50)])
    email = EmailField(label="Email", validators=[Email()])
    verify_email = EmailField(label="Verify Email", validators=[EqualTo("email", "The emails must Match")])
    submit = SubmitField(label="Add Owner")
