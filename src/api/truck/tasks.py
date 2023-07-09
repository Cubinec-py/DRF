from celery import shared_task
from random import choice

from api.truck.models import Truck
from api.location.models import Location


@shared_task
def change_truck_location():
    for _ in range(Truck.objects.all().count()):
        location_id = choice(Location.objects.all().values_list('id', flat=True))
        Truck.objects.all().update(location_id=location_id)
