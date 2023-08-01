from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation , authenticate
from Account.models import Student,HOD
from FaceR.models import Org
import datetime


class Sign_up(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm  Password')

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(), 'email': forms.EmailInput()}

        def clean_email(self):
            email= self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).count():
                raise forms.ValidationError('A user with that email already exists.')
            return email


class Log_in(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(),label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

    # def __init__(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        


CHOICES = (
    ("CSE", "CSE"),
    ("ME", "ME"),
    ("CIVIL", "CIVIL"),
    ("EC", "EC"),
)


class HodForm(forms.ModelForm):
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
    passwdd_ = forms.CharField(label='Confirm  Password', widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
    class Meta:
        model = HOD
        fields = ("name","branch")
        widgets ={'name':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'branch':forms.TextInput(attrs ={'class':'form-control form-control-sm'})}

class HodLogin(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs ={'class':'form-control form-control-sm'}))
    branch = forms.CharField(max_length=50,widget=forms.TextInput(attrs ={'class':'form-control form-control-sm'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))

class HODdAttend(forms.Form):
    
    # Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    Batch = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))



class Studentdata(forms.ModelForm):
    
    class Meta: 
        model = Student
        fields = ("name","enrollment","adm_year","image")
        widgets ={'name':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'enrollment':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'adm_year':forms.TextInput(attrs ={'class':'form-control form-control-sm'})}

class DeleteStud(forms.ModelForm):
    
    class Meta: 
        model = Student
        fields = ("name","enrollment","adm_year")
        widgets ={'name':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'enrollment':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'adm_year':forms.TextInput(attrs ={'class':'form-control form-control-sm'})}

class organization(forms.ModelForm):
    class Meta:
        model = Org
        fields = ("name","contact","address","city","state","postalcode","email")
        widgets = {'name':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'contact':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'address':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'city':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'state':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'postalcode':forms.TextInput(attrs ={'class':'form-control form-control-sm'}),'email':forms.EmailInput(attrs={'class':'form-control form-control-sm'})}

class showStu(forms.Form):
    Branch = forms.CharField(max_length=3,widget=forms.TextInput(attrs={"class": "form-control"}))
    Batch = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

class FindAttend(forms.Form):
    Branch = forms.CharField(max_length=3,widget=forms.TextInput(attrs={"class": "form-control"}))
    Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    Batch = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
