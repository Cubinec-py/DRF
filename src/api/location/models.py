from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _


class Location(models.Model):
    city = models.CharField(
        max_length=100,
        verbose_name='City name'
    )
    state = models.CharField(
        max_length=100,
        verbose_name='City state'
    )
    zip = models.CharField(
        max_length=6,
        unique=True,
        validators=[RegexValidator('^[0-9]{6}$', _('Invalid zip code'))],
        verbose_name='City zip code'
    )
    latitude = models.FloatField(
        verbose_name='Latitude'
    )
    longitude = models.FloatField(
        verbose_name='Longitude'
    )

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return f'{self.city}, {self.state}'
