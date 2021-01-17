from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('quantity','name','address','city')
