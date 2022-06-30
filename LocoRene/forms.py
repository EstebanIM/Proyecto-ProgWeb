from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Producto
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'imagen']

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']
