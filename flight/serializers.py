from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation
)

#---------- FixSerializer------

class FixSerializer(serializers.ModelSerializer):
    pass

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