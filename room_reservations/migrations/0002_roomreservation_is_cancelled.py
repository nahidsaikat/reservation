# Generated by Django 3.2.9 on 2021-11-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomreservation',
            name='is_cancelled',
            field=models.BooleanField(default=False, verbose_name='is_cancelled'),
        ),
    ]
