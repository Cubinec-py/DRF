from django.contrib import admin
from api.truck.models import Truck


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    fields = [
        "number",
        "load_capacity",
        "location",
    ]
    search_fields = [
        "number",
        "load_capacity",
    ]
    autocomplete_fields = [
        "location",
    ]
