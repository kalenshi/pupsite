from flask_wtf import FlaskForm
from wtforms import (SubmitField, StringField, IntegerField, TextAreaField, FileField)
from wtforms.validators import Length, NumberRange


class AddPupForm(FlaskForm):
    """
    Form for creating a Pup
    """
    name = StringField(label="Name", validators=[Length(min=3, max=20)])
    breed = StringField(label="Breed", validators=[Length(min=3, max=20)])
    age = IntegerField(label="Age", validators=[NumberRange(min=1, max=20)])
    details = TextAreaField(label="Details")
    picture = FileField(label="Picture", validators=[])
    submit = SubmitField(label="Add Pup")
