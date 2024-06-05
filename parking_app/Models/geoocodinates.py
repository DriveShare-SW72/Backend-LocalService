from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from parking_app.Models.parking_model import Parking

class Geocoordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
