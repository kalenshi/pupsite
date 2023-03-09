from pupsite import db


class Pup(db.Model):
    """
    The Model to represent the Pups on the site
    """
    __tablename__ = "pup"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    breed = db.Column(db.String(20), nullable=False)
    details = db.Column(db.Text(), nullable=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey("member.id"), nullable=True)

    def __int__(self, name, breed, age, owner=None):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def __repr__(self):
        """
        String representation of the pup

        Returns:
            str : the name and id of the pup
        """
        return f"{self.id}: {self.name}"
