from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VehicleManager(models.Manager):
    def approved(self):
        return self.filter(approval_status='approved')
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
    approval_status = models.CharField(max_length=20, default='pending')
    #vehicle_id=models.IntegerField(primary_key=True,blank=False,null=False)
    number_plate = models.CharField(max_length=20, blank=True, null=True)
    distance_travelled=models.DecimalField(max_digits=10,default=0,decimal_places=0)
    images=models.ImageField(upload_to='images/',default="default.jpg",blank=False)
    mileage=models.DecimalField(max_digits=10,default=0,decimal_places=0)
    cost=models.IntegerField(null=True,blank=True)
    available_status=models.CharField(max_length=2,default='NB',choices=AVAILABE_CHOICES)
    insurance_status=models.CharField(max_length=2,default='NU',choices=INSURANCES_CHOICES)
    fuel=models.CharField(max_length=1,default='D',choices=FUEL_CHOICES)

    #def __str__(self):
      #return self.number_plate
    objects = VehicleManager()



         
        