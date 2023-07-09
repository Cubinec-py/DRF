from rest_framework import serializers

from api.cargo.models import Cargo
from api.location.models import Location
from api.location.serializers import ZipCodeField
from api.truck.models import Truck
from api.truck.serializers import TruckSerializer


from geopy import distance


class CargoSerializer(serializers.ModelSerializer):
    location_pick_up = ZipCodeField(help_text='Zip cod of cargo pick-up location')
    location_delivery = ZipCodeField(help_text='Zip cod of cargo delivery location')
    trucks_near = serializers.SerializerMethodField()

    def get_trucks_near(self, instance):
        trucks = Truck.objects.all()
        serializer = TruckSerializer(instance=trucks, many=True)
        track_serializer = []
        for track in serializer.data:
            city = track['location'].split(',')[0]
            state = track['location'].split(', ')[1]
            truck_location = (
                Location.objects.filter(city=city).first().latitude,
                Location.objects.filter(city=city).first().longitude
            )
            distance_to_cargo = round(distance.distance(
                (instance.location_pick_up.latitude, instance.location_pick_up.longitude),
                truck_location
            ).miles)
            if distance_to_cargo <= 450:
                track['distance_to_cargo'] = distance_to_cargo
                track.pop('location')
                track.pop('load_capacity')
                track_serializer.append(track)
        return track_serializer if len(track_serializer) > 0 else None

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
        fields = ['weight', 'description', 'location_pick_up', 'location_delivery', 'trucks_near']
