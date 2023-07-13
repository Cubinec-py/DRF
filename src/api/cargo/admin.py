from django.contrib import admin
from api.cargo.models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    fields = [
        "weight",
        "description",
        "location_pick_up",
        "location_delivery",
    ]
    search_fields = [
        "weight",
        "location_pick_up",
        "location_delivery",
    ]

    autocomplete_fields = [
        "location_pick_up",
        "location_delivery",
    ]
