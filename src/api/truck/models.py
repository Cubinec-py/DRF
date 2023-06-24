from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from src.api.location.models import Location


class Truck(models.Model):
    number = models.CharField(
        max_length=10,
        unique=True,
        help_text=
        'Digit from 1000 to 9999 + random capital English letter at the end, example: "1234A", "2534B", "9999Z"',
        verbose_name='Truck number'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='trucks_location',
        verbose_name='Location',
    )
    load_capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                1,
                message='Min truck load capacity must be 1'
            ),
            MaxValueValidator(
                10000,
                message='Max truck load capacity must be 10000'
            )
        ],
        verbose_name='Truck load capacity',
        help_text='Truck load capacity must be between 1 and 10000'
    )

    class Meta:
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'

    def __str__(self):
        return f'Truck number: {self.number}, truck load capacity: {self.load_capacity}'
