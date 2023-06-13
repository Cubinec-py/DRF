from rest_framework import serializers

from api.cargo.models import Cargo
from api.location.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ZipCodeField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            location = Location.objects.get(zip=data)
            return location
        except Location.DoesNotExist:
            raise serializers.ValidationError("Invalid zip code")


class CargoSerializer(serializers.ModelSerializer):
    location_pick_up = ZipCodeField()
    location_delivery = ZipCodeField()

    def validate(self, data):
        if data.get('location_pick_up') and data.get('location_delivery'):
            location_pick_up = data.get('location_pick_up')
            location_delivery = data.get('location_delivery')

            if location_pick_up == location_delivery:
                raise serializers.ValidationError(
                    "Pick-up and delivery locations cannot be the same"
                )
        elif data.get('location_pick_up') and data.get('location_pick_up') == self.instance.location_delivery:
            raise serializers.ValidationError(
                f"Pick-up and delivery location cannot be the same"
            )
        elif data.get('location_delivery'):
            raise serializers.ValidationError(
                f"Delivery and pick-up location cannot be the same"
            )

        return data

    def update(self, instance, validated_data):
        instance.weight = validated_data.get('weight', instance.weight)
        instance.description = validated_data.get('description', instance.description)
        instance.location_pick_up = validated_data.get('location_pick_up', instance.location_pick_up)
        instance.location_delivery = validated_data.get('location_delivery', instance.location_delivery)
        instance.save()
        return instance

    class Meta:
        model = Cargo
        fields = ['weight', 'description', 'location_pick_up', 'location_delivery']
