from celery import shared_task
from random import choice

from src.api.truck.models import Truck
from src.api.location.models import Location


@shared_task
def change_truck_location():
    Truck.objects.all().update(location_id=choice(Location.objects.all().values_list('id', flat=True)))
