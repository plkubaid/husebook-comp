from django import forms
from .models import support,suggestionM



class OpenSupport(forms.ModelForm):
    class Meta:
        model = support
        fields = [
        'email',
        'body'
        ]


class CustomerSupport(forms.ModelForm):
    class Meta:
        model = support
        fields = [
        'body'
        ]

class Suggestion(forms.ModelForm):
    class Meta:
        model = suggestionM
        fields = [
        'body'
        ]
