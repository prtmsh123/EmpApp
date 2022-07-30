from dataclasses import field, fields
from tkinter import Widget
from unicodedata import name
from django import forms
from django.core import validators
from .models import Register, User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','contact']
        Widgets = {
            
            
            'name': forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Z a-z ]+', 'title':'Enter Characters Only '}),
            'email': forms.EmailInput(attrs={'class':"form-control"}),
           # 'password': forms.PasswordInput(render_value=True,attrs={'class':"form-control"}),
            'contact':forms.NumberInput(attrs={'class':"form-control"}),


        }
    

class Loginpage(forms.ModelForm):
    class Meta:
        fields=['name','password']
        Widget = {
            'name': forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Z a-z ]+', 'title':'Enter Characters Only '}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':"form-control"}),

        }
class EmployeeRegister(forms.ModelForm):


     class Meta:

        model=Register
        fields=['first_name','last_name','username','email','password1','password2']
        Widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Z a-z ]+', 'title':'Enter Characters Only '}),
            'last_name': forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Z a-z ]+', 'title':'Enter Characters Only '}),
            'username': forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Z a-z ]+', 'title':'Enter Characters Only '}),
            'email': forms.EmailInput(attrs={'class':"form-control"}),
           'password1': forms.PasswordInput(render_value=True,attrs={'class':"form-control"}),
           'password1': forms.PasswordInput(render_value=True,attrs={'class':"form-control"}),

        }

 