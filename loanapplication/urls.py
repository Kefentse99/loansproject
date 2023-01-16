from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [ 

    path('', views.homepage ,name="homepage"),
    
    path('homepage/', views.homepage ,name="homepage"),

    path('dataprocessing/', views.createForm ,name="dataprocessing"),

    path('datasumary/', views.customers ,name="datasumary"), 

    path('update_user/<str:pk>/', views.updateForm ,name="update_user"),
    
    path('deletePage/<str:pk>/', views.deleteCustomer ,name="deletePage"),

   
]