import email
from attr import attr
from django.contrib.auth.forms import UserCreationForm
from user.models import KhachHang
from django import forms
from products.models import User

class CustomerUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter email"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter confirm password"}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
