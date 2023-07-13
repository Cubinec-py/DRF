from django.contrib import admin
from api.location.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = [
        "city",
        "state",
        "zip",
        "latitude",
        "longitude",
    ]
    search_fields = [
        "city",
        "state",
        "zip",
    ]
