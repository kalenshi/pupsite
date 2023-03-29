import factory
from faker import Faker

from pupsite.models import Pup
from tests.factories.base_factory import BaseFactory
from tests.factories.member import MemberFactory

faker = Faker()
breeds = [
    "German Shepherd",
    "Bulldog",
    "Labrador Retriever",
    "Golden Retriever",
    "French Bulldog",
    "Siberian Husky",
    "Alaskan Malamute",
    "Poodle",
    "Chihuahua",
    "Border Collie",
    "Afghan Hound",
    "Airedale Terrier"
]
picture_extensions = [".png", ".jpeg", ".jpg", ".gif", ".psd", ".tiff"]


class PupFactory(BaseFactory):
    """
    Factory for creating Pup instances
    """

    class Meta:
        model = Pup

    id = factory.sequence(lambda n: n)
    name = faker.name
    age = faker.random.randint(1, 13)
    breed = faker.random.choice(breeds)
    details = faker.paragraph(5)
    owner_id = factory.SubFactory(MemberFactory)
    picture = "default.png"
