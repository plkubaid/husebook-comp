from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Pform(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['first_name','last_name','email','business','profile_picture']


class CustomForm(UserCreationForm):
    email= forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')


    def save(self,commit=True):
        user = super(CustomForm,self).save(commit=False)
        user.email = cleaned_data('email')
        user.first_name = cleaned_data('first_name')
        user.last_name = cleaned_data('last_name')
        if commit:
            user.save()
        return user
