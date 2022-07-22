from django import forms
from django.forms import ModelForm
from .models import Local, Categoria, Item


class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = '__all__'


class CategoriaForm(ModelForm):
    class Meta:
        model = Local
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Local
        fields = '__all__'
