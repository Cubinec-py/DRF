from rest_framework import serializers

from api.truck.models import Truck
from api.location.serializers import ZipCodeField


class TruckSerializer(serializers.ModelSerializer):
    location = ZipCodeField(help_text='Zip cod of truck location')

    def validate(self, data):
        if data.get('location'):
            location = data.get('location')
            if self.instance.location == location:
                raise serializers.ValidationError(
                    "Truck is already here"
                )
        elif data.get('number'):
            number = data.get('number')

            if self.instance.number == number:
                raise serializers.ValidationError(
                    "Truck is already have this number"
                )
            elif Truck.objects.filter(number=number).exists():
                raise serializers.ValidationError(
                    "Truck with such number already exists"
                )

        return data

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.location = validated_data.get('location', instance.location)
        instance.load_capacity = validated_data.get('load_capacity', instance.load_capacity)
        instance.save()
        return instance

    class Meta:
        model = Truck
        fields = ['number', 'location', 'load_capacity']
