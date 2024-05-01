from django import forms

class VehicleRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    number_plate = forms.CharField(max_length=20)
    distance_travelled = forms.DecimalField(max_digits=10, decimal_places=0)
    images = forms.ImageField()
    mileage = forms.DecimalField(max_digits=10, decimal_places=0)
    cost = forms.IntegerField()
