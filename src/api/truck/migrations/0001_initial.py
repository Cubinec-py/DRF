# Generated by Django 4.2.2 on 2023-06-13 15:19

import django.core.validators
import django.db.models.deletion

from django.db import migrations, models
from random import randint, choice

from api.truck.models import Truck
from api.location.models import Location


def forward_func(apps, schema_editor):
    trucks = []
    number = set()
    for _ in range(500):
        truck_num = randint(1000, 9999)
        truck_letter = chr(randint(ord("A"), ord("Z")))
        load_capacity = randint(1, 10000)
        location_id = choice(Location.objects.all().values_list("id", flat=True))
        truck_number = f"{truck_num}{truck_letter}"
        if truck_number not in number:
            number.add(truck_number)
            trucks.append(
                Truck(
                    number=f"{truck_num}{truck_letter}",
                    load_capacity=load_capacity,
                    location_id=location_id,
                )
            )
    Truck.objects.bulk_create(trucks)


def reverse_func(apps, schema_editor):
    Truck.objects.all().delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Truck",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        help_text='Digit from 1000 to 9999 + random capital English letter at the end, example: "1234A", "2534B", "9999Z"',
                        max_length=10,
                        unique=True,
                        verbose_name="Truck number",
                    ),
                ),
                (
                    "load_capacity",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="Min truck load capacity must be 1"
                            ),
                            django.core.validators.MaxValueValidator(
                                10000, message="Max truck load capacity must be 10000"
                            ),
                        ],
                        verbose_name="Truck load capacity",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trucks_location",
                        to="location.location",
                        verbose_name="Location",
                    ),
                ),
            ],
            options={
                "verbose_name": "Truck",
                "verbose_name_plural": "Trucks",
            },
        ),
        migrations.RunPython(code=forward_func, reverse_code=reverse_func),
    ]
