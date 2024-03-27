from django.shortcuts import render
from .models import Vehicle
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.



@login_required
def Rentvehicle(request):
    user = request.user
    if request.method == 'POST':
        # Ensure 'owner' key exists in the POST data
            name=request.POST.get('name')
            number_plate = request.POST.get('number_plate')
            distance_travelled = request.POST.get('distance_travelled')
            images = request.FILES.get('images')
            mileage = request.POST.get('mileage')
            cost = request.POST.get('cost')
            insurance_status = request.POST.get('insurance_status')
            fuel = request.POST.get('fuel')

            new_vehicle = Vehicle(
                owner=user,
                name=name,
                number_plate=number_plate,
                distance_travelled=distance_travelled,
                images=images,
                mileage=mileage,
                cost=cost,
                insurance_status=insurance_status,
                fuel=fuel,
                approval_status='pending'
            )
            new_vehicle.save()
            return HttpResponseRedirect(reverse('rent'))

    return render(request, 'rent.html')


@login_required
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

@login_required
def rent_page_view(request):
    
    return render(request, 'rent.html')
