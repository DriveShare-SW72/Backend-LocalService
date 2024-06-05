from rest_framework import serializers
from parking_app.Models.geoocodinates import Parking, Geocoordinates
from parking_app.Models.location_model import Location
from parking_app.Models.schedule_model import Schedule
from parking_app.Models.review_model import Review

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class GeocoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geocoordinates
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'