from flask_wtf import FlaskForm
from wtforms import (SubmitField, StringField, IntegerField, TextAreaField, FileField)
from wtforms.validators import Length, NumberRange, DataRequired

from pupsite.utils.picture_utils import validate_picture_format


class AddPupForm(FlaskForm):
    """
    Form for creating a Pup
    """
    name = StringField(label="Name", validators=[Length(min=3, max=20), DataRequired()])
    breed = StringField(label="Breed", validators=[Length(min=3, max=20), DataRequired()])
    age = IntegerField(label="Age", validators=[NumberRange(min=1, max=20), DataRequired()])
    details = TextAreaField(label="Details", validators=[DataRequired()])
    picture = FileField(label="Picture", validators=[validate_picture_format])
    submit = SubmitField(label="Add Pup")
