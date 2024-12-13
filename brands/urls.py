from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.brand_list, name='brand_list'),
]
