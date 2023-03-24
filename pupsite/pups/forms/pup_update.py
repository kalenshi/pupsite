from flask_wtf import FlaskForm
from wtforms import (SubmitField, StringField, IntegerField, TextAreaField, FileField)
from wtforms.validators import Length, NumberRange


class UpdatePupForm(FlaskForm):
    """
    Form for creating a Pup
    """
    breed = StringField(label="Breed", validators=[Length(min=3, max=20)])
    age = IntegerField(label="Age", validators=[NumberRange(min=1, max=20)])
    details = TextAreaField(label="Details")
    picture = FileField(label="Picture", validators=[])
    update = SubmitField(label="Update Pup")
