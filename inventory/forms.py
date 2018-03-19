from django import forms
from .models import Inventory


class InventoryAdd(forms.ModelForm):
    class Meta:
        model=Inventory
        fields = ['code','name','price','quantity','danger_level']


class InventoryUpdate(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['code','price','quantity']
