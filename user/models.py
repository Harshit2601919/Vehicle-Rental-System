from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=10)
    email = models.EmailField()
    contact_no=models.IntegerField(max_digits=10)
    address=models.TextField()
    DOB=models.DateField()
    addhar_card=models.IntegerField(unique=True)
    age=models.IntegerField(max_digits=3)
    driving_liscense=models.CharField(max_length=100,null=False,unique=True)
    def __str__(self):
        return self.name 
    