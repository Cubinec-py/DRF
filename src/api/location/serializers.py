from rest_framework import serializers
from src.api.location.models import Location


class ZipCodeField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            location = Location.objects.get(zip=data)
            return location
        except Location.DoesNotExist:
            raise serializers.ValidationError("Invalid zip code")


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
