from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Location(models.Model):
    type = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    address = models.TextField()
    address_number = models.CharField(max_length=20)