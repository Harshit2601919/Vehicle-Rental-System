from django.urls import path
from . import views

urlpatterns = [

    path('rent/',views.Rentvehicle,name='rent'),
    path('book/',views.Bookvehicle,name='book'),
    path('rent_history/',views.rent_history,name='rent_history'),
    path('rent_html/', views.rent_page_view, name='rent_page'),
    
]