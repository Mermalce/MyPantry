from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Item


def home_page_view(request):
    return render(request, 'MyPantry/home.html')


def inventario_view(request):
    context = {'items': Item.objects.all()}
    return render(request, 'MyPantry/inventario.html', context)
