import email
from pyexpat import model
from tkinter import Widget
from django.db import models
from django.core.validators import RegexValidator



alphanumeric1 = RegexValidator( r'^[a-z A-Z]*$', 'Only alphabet characters are allowed.' )

alphanumeric = RegexValidator( r'^[a-z A-Z]*$', 'Only alphabet characters are allowed.' )

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric1])
    email=models.EmailField(max_length=100)
    #password=models.CharField(max_length=50)
    contact=models.BigIntegerField(default=None)
# login
class Register(models.Model):
    first_name=models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric1])
    last_name=models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric1])
    username=models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric1])
    email=models.EmailField(max_length=50)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)





class Login(models.Model):
        name=models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
        password=models.CharField(max_length=20)

    