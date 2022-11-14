
from .models import PhoneNumber
from django import forms

from django.forms import fields


class PhoneNumber(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone']