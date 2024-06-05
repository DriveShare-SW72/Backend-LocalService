from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()