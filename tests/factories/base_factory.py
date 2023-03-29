from factory.alchemy import SQLAlchemyModelFactory
from pupsite import db


class BaseFactory(SQLAlchemyModelFactory):
    """
    The base factory that ensures that the needed SQLAlchemy
    sessions object is added to the meta class
    """

    class Meta:
        abstract = True
        sqlalchemy_session = db.session
