from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from parking_app.Models.location_model import Location
from parking_app.Models.schedule_model import Schedule
from parking_app.Enums.parking_status import ParkingStatus
class Parking(models.Model):
    owner_id = models.CharField(max_length=100)

    description = models.CharField(max_length=100)
    address = models.TextField()
    address_number = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=15,
        choices=[(status.name, status.value) for status in ParkingStatus],
        default=ParkingStatus.AVAILABLE.value
    )
    phone_service = models.CharField(max_length=15)
    price_per_hour = models.FloatField()

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
