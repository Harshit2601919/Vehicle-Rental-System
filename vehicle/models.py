from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicle(models.Model):


    AVAILABE_CHOICES=(
        ('B', 'Booked'),
        ('NB', 'Not Booked'),
    )

    INSURANCES_CHOICES=(
        ('U','Updated'),
        ('NU', 'No Update'),
    )

    FUEL_CHOICES=(
    ('P', 'Petrol'),
    ('D', ' Diesel'),
     )

    owner = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    number_plate=models.CharField(max_length=100)
    distance_travelled=models.DecimalField(max_digits=10,default=0,decimal_places=0)
    images=models.ImageField(upload_to='',default="default.png",blank=False)
    mileage=models.DecimalField(max_digits=10,default=0,decimal_places=0)
    cost=models.IntegerField(null=True,blank=True)
    available_status=models.CharField(max_length=2,default='NB',choices=AVAILABE_CHOICES)
    insurance_status=models.CharField(max_length=2,default='NU',choices=INSURANCES_CHOICES)
    fuel=models.CharField(max_length=1,default='D',choices=FUEL_CHOICES)

    