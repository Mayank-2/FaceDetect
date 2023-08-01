from django.contrib.auth.models import User
from django import forms

class Dash(forms.Form):
    Branch = forms.CharField(max_length=3,widget=forms.TextInput(attrs={"class": "form-control"}))
    Batch = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
