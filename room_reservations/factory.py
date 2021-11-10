from datetime import datetime

import factory
from faker import Faker
from factory.django import DjangoModelFactory

from employees.factory import EmployeeFactory
from room_reservations.models import RoomReservation

fake = Faker()


class RoomReservationFactory(DjangoModelFactory):
    class Meta:
        model = RoomReservation

    title = factory.LazyAttribute(lambda a: fake.name())
    from_date = factory.LazyFunction(datetime.now().date)
    to_date = factory.LazyFunction(datetime.now().date)
    employee = factory.SubFactory(EmployeeFactory)
