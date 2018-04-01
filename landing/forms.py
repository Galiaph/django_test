from django import forms
from .models import *

class SubsctiberForms(forms.ModelForm):
    class Meta():
        model = Subscribers
        exclude = [""]
