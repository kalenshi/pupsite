from pupsite import db, bcrypt
from flask_login import UserMixin, current_user
from pupsite import db, login_manager


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

    def verify_password(self, password):
        """
        Checks that the password hash provided is the right password for the member

        Args:
            password(str): password to be checked

        Returns:
            bol : True if password matches , false otherwise

        """
        return bcrypt.check_password_hash(self.password, password)
