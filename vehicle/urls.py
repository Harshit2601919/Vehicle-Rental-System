from django.urls import path

from . import views

urlpatterns = [

    path('rent/',views.Rentvehicle,name='rent'),
    path('book/',views.Bookvehicle,name='book'),

]