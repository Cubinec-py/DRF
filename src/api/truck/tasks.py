from celery import shared_task
from random import choice

from api.truck.models import Truck
from api.location.models import Location


@shared_task
def change_truck_location():
    locations = Location.objects.all().values_list("id", flat=True)
    trucks = Truck.objects.all()
    for truck in trucks:
        location_id = choice(locations)
        truck.location_id = location_id
    Truck.objects.bulk_update(trucks, ["location_id"])
