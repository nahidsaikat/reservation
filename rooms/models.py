from django.db import models


class Room(models.Model):
    name = models.CharField("name", max_length=100)
