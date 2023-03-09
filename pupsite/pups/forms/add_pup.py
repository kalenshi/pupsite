from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Length, NumberRange, ValidationError

from pupsite import db
from pupsite.models import Member


class AddPupForm(FlaskForm):
    """
    Form for creating a Pup
    """
    name = StringField(label="Name", validators=[Length(min=3, max=20)])
    breed = StringField(label="Breed", validators=[Length(min=3, max=20)])
    age = IntegerField(label="Age", validators=[NumberRange(min=1, max=20)])
    details = TextAreaField(label="Details")
    owner = SelectField(label="Owner", choices=[1, 2])
    submit = SubmitField(label="Add Pup")

    def validate_owner(self, owner):
        """
        Validates the owner against members in the database

        Args:
            owner(int): the primary key of the owner to validate

        Returns:
            int : the integer primary key if the owner is a valid member

        Throws:
            ValidationError: Throws validation error if a member with a given id does not exist
        """
        if db.session.get(Member, owner.data):
            return owner
        else:
            raise ValidationError(f"Member with id {owner.data} Does not exist in our Database")

    @classmethod
    def get_owners(cls):
        """
        Retrieve a List of members' ids from the database

        Returns:
            list : a list of member ids
        """
        return [member.id for member in db.session.get(Member)]
