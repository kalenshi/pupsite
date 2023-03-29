import factory
from factory import Faker

from pupsite.models import Member
from tests.factories.base_factory import BaseFactory


class MemberFactory(BaseFactory):
    """
    Factory for creating Member instances
    """

    class Meta:
        model = Member

    id = factory.sequence(lambda n: n + 1)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    password = Faker("password")
