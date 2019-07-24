from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    
]







urlpatterns+=[
    path('home/', views.home, name='home'),
]
