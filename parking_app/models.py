from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Location(models.Model):
    type = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    address = models.TextField()
    address_number = models.CharField(max_length=20)

class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

class Parking(models.Model):
    owner_id = models.CharField(max_length=100)

    description = models.CharField(max_length=100)
    address = models.TextField()
    address_number = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    phone_service = models.CharField(max_length=15)
    price_per_hour = models.FloatField()

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

class Review(models.Model):
    user_id = models.CharField(max_length=100)

    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

class Geocoordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
