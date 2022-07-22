from django.shortcuts import render
from django.urls import path

from . import views

app_name = "MyPantry"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('inventario/', views.inventario_view, name='inventario')
]
