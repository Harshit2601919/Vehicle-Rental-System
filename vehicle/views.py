from django.shortcuts import render

# Create your views here.


    
def Rentvehicle(request):
    return render(request,'rent.html')


def Bookvehicle(request):
    
    return render(request,'book.html')