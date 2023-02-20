from django import forms
from .models import *


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['title', 'category', 'text', 'file', ]


class CreateResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['message', ]
