import email
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import StudentRegistration
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
# this function for add new item and show all data
def add_show(request):
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            #pw=fm.cleaned_data['password']
            cn=fm.cleaned_data['contact']
            reg=User(name=nm,email=em,contact=cn)
            reg.save()
            fm=StudentRegistration()
            
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

###
def addemp(request):
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            #pw=fm.cleaned_data['password']
            cn=fm.cleaned_data['contact']
            reg=User(name=nm,email=em,contact=cn)
            reg.save()
            fm=StudentRegistration()
            return HttpResponseRedirect('/')

            
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addemp.html',{'form':fm,'stu':stud})


        
            

#this function for update and edit
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm= StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else: 
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})


 #this function for delate data   
def deletedata(request,id):
    if request.method =='POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def register(request):
    if request.method == "POST":


        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()



    return render(request,'enroll/register.html', {'form':form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('addandshow')
    else:
        form = AuthenticationForm()

    return render(request,'enroll/login.html',{'form':form})
