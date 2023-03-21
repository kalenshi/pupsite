from datetime import datetime, timedelta

import jwt

from flask import current_app
from flask_login import UserMixin

from pupsite import db, login_manager, bcrypt


@login_manager.user_loader
def load_user(member_id):
    """
    Login the User to the site

    Returns:
        The member of the site
    """
    return db.get_or_404(Member, member_id)


class Member(db.Model, UserMixin):
    """
    The Model to represent the Pups on the site
    """
    __tablename__ = "member"
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    pets = db.relationship("Pup", backref="owner", lazy=True)

    def __int__(self, first_name, last_name, email, password, *args, **kwargs):
        super(Member, self).__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        """
        String representation of the pup

        Returns:
            str : the name and id of the pup
        """
        return f"{self.id}: {self.email}"

    @staticmethod
    def set_password(password: str) -> str:
        """
        Hashes the password for storing in the database

        Args:
            password(str): the password string to bre hashed

        Returns:
            str : The hashed password
        """
        return bcrypt.generate_password_hash(password)  # .decode("utf-8")

    def verify_password(self, password: str) -> bool:
        """
        Checks that the password hash provided is the right password for the member

        Args:
            password(str): password to be checked

        Returns:
            bol : True if password matches , false otherwise

        """
        return bcrypt.check_password_hash(self.password, password)

    def get_reset_token(self, ttl: int = 1800) -> str:
        """
        Creates a token to use in authenticating a password rest request

        Args:
            ttl (int): Time in seconds before the token expires (time to live)

        Returns:
            str : An encoded string containing the user's ID

        """
        payload = {
            "member_id": self.id,
            "exp": datetime.utcnow() + timedelta(seconds=ttl)
        }
        token = jwt.encode(
            payload=payload,
            key=current_app.config.get("SECRET_KEY"),
            algorithm="HS256"
        )
        return token

    @staticmethod
    def verify_reset_token(token_hash: str) -> object:
        """
        Verifies the identity of the user with the provided token
        Args:
            token_hash (str): An encoded token with user data

        Returns:
            object : An instance of the member if verified  None otherwise
        """
        try:
            serialized = jwt.decode(
                jwt=token_hash,
                key=current_app.config.get("SECRET_KEY"),
                algorithms=["HS256"]
            )
            return db.get_or_404(Member, serialized.get("member_id"))
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
            return None
