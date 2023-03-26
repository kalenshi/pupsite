from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField, PasswordField
from wtforms.validators import Email, EqualTo, Length, DataRequired


class MemberForm(FlaskForm):
    """
    Form for creating New members on the pup site
    """
    first_name = StringField(label="First Name", validators=[Length(min=2, max=50), DataRequired()])
    last_name = StringField(label="Last Name", validators=[Length(min=2, max=50), DataRequired()])
    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    verify_email = EmailField(
        label="Verify Email",
        validators=[EqualTo("email", "The emails must Match"), DataRequired()]
    )
    password = PasswordField(label="Password", validators=[Length(min=6, max=40), DataRequired()])
    verify_password = PasswordField(
        label="Verify Password", validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField(label="Add Member")
