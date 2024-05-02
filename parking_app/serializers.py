from rest_framework import serializers
from parking_app.models import Parking, Location, Schedule, Review
from parking_app.models import Geocoordinates

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