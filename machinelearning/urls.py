from django.urls import path 
from . import views

urlpatterns = [ 
    path('bankstaff/', views.emps , name="bankstaff"),  
    path('account/', views.account , name="account"), 
    path('bio/<str:pk>/', views.bios ,name="bio"),
    path('register/', views.registerPage , name="register"),
    path('login/', views.loginPage , name="login"), 
    path('logout/', views.logoutUser , name="logout"),
]