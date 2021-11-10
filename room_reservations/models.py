from django.db import models

from employees.models import Employee


class RoomReservation(models.Model):
    title = models.CharField("title", max_length=100)
    from_date = models.DateField("from_date")
    to_date = models.DateField("to_date")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    is_cancelled = models.BooleanField("is_cancelled", default=False)
