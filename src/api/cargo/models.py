from django.db import models
from src.api.location.models import Location
from django.core.validators import MaxValueValidator, MinValueValidator


class Cargo(models.Model):
    location_pick_up = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='cargo_pick_up',
        verbose_name='Cargo pick-up location',
    )
    location_delivery = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='cargo_delivery',
        verbose_name='Cargo delivery location',
    )
    weight = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                limit_value=1
            ),
            MaxValueValidator(
                limit_value=10000
            ),
        ],
        verbose_name='Cargo load capacity',
        help_text='Cargo load capacity must be between 1 and 10000',
    )
    description = models.TextField(
        max_length=250,
        verbose_name='Cargo description',
        help_text='Description of cargo',
    )

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargo'

