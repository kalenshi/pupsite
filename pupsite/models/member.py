from pupsite import db


class Member(db.Model):
    """
    The Model to represent the Pups on the site
    """
    __tablename__ = "member"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    pets = db.relationship("Pup", backref="owner", lazy=True)

    def __int__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        """
        String representation of the pup

        Returns:
            str : the name and id of the pup
        """
        return f"{self.id}: {self.email}"
