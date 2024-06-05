from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from parking_app.Models.parking_model import Parking

class Review(models.Model):
    user_id = models.CharField(max_length=100)

    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
