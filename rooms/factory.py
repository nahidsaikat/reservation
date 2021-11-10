from faker import Faker
from factory.django import DjangoModelFactory

from rooms.models import Room

fake = Faker()


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    name = fake.name()
