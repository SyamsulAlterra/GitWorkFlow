from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
   path('author',views.author_view,name="author") 
]