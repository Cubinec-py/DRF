from collections import OrderedDict
from django.core.validators import MaxValueValidator, MinValueValidator

from rest_framework import serializers

from api.cargo.models import Cargo
from api.location.models import Location
from api.location.serializers import ZipCodeField
from api.truck.models import Truck


from geopy import distance


class MyParametersSerializer(serializers.Serializer):
    weight = serializers.IntegerField(
        required=False,
        min_value=1,
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=10000),
        ],
        max_value=10000,
        help_text="Cargo load capacity must be integer and between 1 - 10000",
    )
    trucks_near = serializers.IntegerField(
        required=False, help_text="Miles of trucks near, only integer"
    )


class CargoSerializer(serializers.ModelSerializer):
    location_pick_up = ZipCodeField(help_text="Zip cod of cargo pick-up location")
    location_delivery = ZipCodeField(help_text="Zip cod of cargo delivery location")
    trucks_near = serializers.SerializerMethodField()

    def get_trucks_near(self, instance: Cargo()):
        miles = 450 if "trucks_near" not in instance.__dict__ else instance.trucks_near
        print("miles", miles)
        trucks = Truck.objects.select_related("location").all().defer("load_capacity")
        track_serializer = []
        for track in trucks:
            truck_location = Location.objects.filter(id=track.location.id).values_list(
                "latitude", "longitude"
            )
            distance_to_cargo = round(
                distance.distance(
                    (
                        instance.location_pick_up.latitude,
                        instance.location_pick_up.longitude,
                    ),
                    truck_location,
                ).miles
            )
            if distance_to_cargo <= miles:
                track_serializer.append(
                    OrderedDict(
                        [
                            ("number", track.number),
                            ("distance_to_cargo", distance_to_cargo),
                        ]
                    )
                )
        return track_serializer if len(track_serializer) > 0 else None

    def validate(self, data):
        if data.get("location_pick_up") and data.get("location_delivery"):
            location_pick_up = data.get("location_pick_up")
            location_delivery = data.get("location_delivery")

            if location_pick_up == location_delivery:
                raise serializers.ValidationError(
                    "Pick-up and delivery locations cannot be the same"
                )
        elif (
            data.get("location_pick_up")
            and data.get("location_pick_up") == self.instance.location_delivery
        ):
            raise serializers.ValidationError(
                "Pick-up and delivery location cannot be the same"
            )
        elif data.get("location_delivery"):
            raise serializers.ValidationError(
                "Delivery and pick-up location cannot be the same"
            )

        return data

    def update(self, instance, validated_data):
        instance.weight = validated_data.get("weight", instance.weight)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    class Meta:
        model = Cargo
        fields = [
            "weight",
            "description",
            "location_pick_up",
            "location_delivery",
            "trucks_near",
        ]


class PatchCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ["weight", "description"]
