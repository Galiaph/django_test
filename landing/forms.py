from django import forms
from .models import Subscribers

class SubsctiberForms(forms.ModelForm):
    class Meta():
        model = Subscribers
        exclude = [""]
