from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faq(models.Model):
    titlePrev = models.CharField(max_length=20, null=True)
    content   = models.TextField(max_length=375,null=True, blank=True)
    question  = models.CharField(max_length=60, null=True)

    def __str__(self):
	    return self.titlePrev

class Customer(models.Model):
    user            = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # Remove related_name here
    name            = models.CharField(max_length=50, null=True)
    phone           = models.CharField(max_length=12, null=True)
    email           = models.CharField(max_length=25, null=True)
    dateCreated     = models.DateTimeField(auto_now_add=True, null=True)
    profilePic      = models.ImageField(default="basicUser.jpg",null=True, blank=True)
   

    def __str__(self):
        return self.name

