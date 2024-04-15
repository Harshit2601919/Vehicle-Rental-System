from django.db import models
from django.contrib.auth.models import User

class VehicleManager(models.Manager):
    def approved(self):
        return self.filter(approval_status='approved')

class Vehicle(models.Model):
    AVAILABE_CHOICES = (
        ('B', 'Booked'),
        ('NB', 'Not Booked'),
    )

    INSURANCES_CHOICES = (
        ('U', 'Updated'),
        ('NU', 'No Update'),
    )

    FUEL_CHOICES = (
        ('P', 'Petrol'),
        ('D', 'Diesel'),
    )

    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=20, default='pending')
    name = models.CharField(max_length=100, null=True, blank=True)
    number_plate = models.CharField(max_length=20, blank=True, null=True)
    distance_travelled = models.DecimalField(max_digits=10, default=0, decimal_places=0)
    images = models.ImageField(upload_to='images/', default="default.jpg", blank=False)
    mileage = models.DecimalField(max_digits=10, default=0, decimal_places=0)
    cost = models.IntegerField(null=True, blank=True)
    available_status = models.CharField(max_length=2, default='NB', choices=AVAILABE_CHOICES)
    insurance_status = models.CharField(max_length=2, default='NU', choices=INSURANCES_CHOICES)
    fuel = models.CharField(max_length=1, default='D', choices=FUEL_CHOICES)
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='vehicles') 

    objects = VehicleManager()

    def __str__(self):
        return self.number_plate




#un appplied models -------------------------------------------------------------------------
class Location(models.Model):
    pickUpPlace = models.CharField(max_length=105, null=True)

    def __str__(self):
        return self.pickUpPlace 

class Order(models.Model):
    customer = models.CharField(max_length=70, null=True)
    customerID = models.CharField(max_length=50, null=True)
    carModel = models.CharField(max_length=70, null=True)
    automobileId = models.CharField(null=True, max_length=10)
    price = models.IntegerField(null=True, blank=False)
    startRent = models.DateField(auto_now_add=False, null=True)
    endRent = models.DateField(auto_now_add=False, null=True)
    orderDate = models.DateTimeField(auto_now_add=True, null=True)
    pickUp = models.ForeignKey(Location, on_delete=models.CASCADE, null=True) 
    insurance = models.BooleanField(blank=True, null=True, default=False)
    payed = models.BooleanField(null=True, default=False)

    def __int__(self):
        return self.id

class canceledOrders(models.Model):
    customerID = models.CharField(max_length=50, null=True)
    automobileId = models.CharField(null=True, max_length=10)
    price = models.IntegerField(null=True, blank=False)
    payed = models.BooleanField(null=True, default=False)

class Faq(models.Model):
    titlePrev = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=375, null=True, blank=True)
    question = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.titlePrev
