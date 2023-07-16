from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation
)

#---------- FixSerializer------

class FixSerializer(serializers.ModelSerializer):

    created = serializers.StringRelatedField()
    created_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)


#---------- Passenger Serializer------

class PassengerSerializer(FixSerializer):
    
    class Meta:
        model=Passenger
        exclude = []

#---------- Flight Serializer------

class FlightSerializer(FixSerializer):
    
    class Meta:
        model= Flight
        exclude = []


#---------- Reservation Serializer------

class ReservationSerializer(FixSerializer):
    
    class Meta:
        model = Reservation
        exclude = []