from django.shortcuts import render,redirect
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.


def registerUser(request):    
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username= data['username'])
            user.set_password(data['password1'])
            user.save()
            return redirect('/?success')
    
    # form = UserCreationForm()
    # context = {
    #     'form': form
    # }
    return render(request,'register.html')

def loginUser(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('/')       
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'login.html',context)