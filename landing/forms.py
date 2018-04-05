from django import forms
from .models import Subscriber

class SubsctiberForms(forms.ModelForm):
    class Meta():
        model = Subscriber
        exclude = [""]
