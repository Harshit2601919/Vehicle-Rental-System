from django.shortcuts import render
from .models import Vehicle
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import *
# Create your views here.



# @login_required
def Rentvehicle(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = VehicleRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                number_plate = form.cleaned_data['number_plate']
                distance_travelled = form.cleaned_data['distance_travelled']
                images = form.cleaned_data['images']
                mileage = form.cleaned_data['mileage']
                cost = form.cleaned_data['cost'] 

                # Set the owner as the username of the logged-in user
                owner = request.user.username

                new_vehicle = Vehicle(
                    owner=owner,
                    name=name,
                    number_plate=number_plate,
                    distance_travelled=distance_travelled,
                    images=images,
                    mileage=mileage,
                    cost=cost, 
                    approval_status='pending'
                )
                new_vehicle.save()
                return HttpResponseRedirect(reverse('rent'))
        else:
            form = VehicleRegistrationForm()
        
        return render(request, 'rent.html', {'form': form})
    else:
        return HttpResponse("Please log in to add a new vehicle.")




# @login_required
def Bookvehicle(request):
    # views.py

    approved_vehicles = Vehicle.objects.filter(approval_status='approved')
    return render(request, 'book.html', {'approved_vehicles': approved_vehicles})


@login_required
def rent_history(request):
     user = request.user
     print(user)
     rent=Vehicle.objects.filter(owner=user)
     
     return render (request,'rent_history.html',{'rent':rent})

# @login_required
def rent_page_view(request):
    
    return render(request, 'rent.html')
