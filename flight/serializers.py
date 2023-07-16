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
    def gender_gender_text(self, obj):
        return obj.get_gender_display()

#---------- Flight Serializer------

class FlightSerializer(FixSerializer):
    
    departure_text = serializers.SerializerMethodField()
    arrival_text = serializers.SerializerMethodField()
    class Meta:
        model= Flight
        fields = (
            "id",
            "created",
            "created_id",
            "departure_text",
            "arrival_text",
            "created_time",
            "updated_time",
            "flight_number",
            "airline",
            "departure",
            "departure_date",
            "arrival",
            "arrival_date",
            "get_airline_display", # dont need SerializerMethodField.
        )

    # SerializerMethodField()
    def get_departure_text(self, obj):
        return obj.get_departure_display()
    
    # SerializerMethodField
    def get_arrival_text(self, obj):
        return obj.get_arrival_display()
    
#---------- Reservation Serializer------

class ReservationSerializer(FixSerializer):
    
    class Meta:
        model = Reservation
        exclude = []