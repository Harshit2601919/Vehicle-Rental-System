from django.db import models
from django.contrib.auth.models import User
from vehicle.models import Vehicle
# Create your models here.


class Review(models.Model):
    review_text=models.TextField()
    