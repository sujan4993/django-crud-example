from django.shortcuts import render,redirect
from employee.models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from customers.models import Customer

def home(request):
    employee = Person.objects.all().count()
    context = {
        'employee':employee
    }
    return render(request,'home.html',context)

def admin_index(request):
    return render(request,'admin-index.html')

def registerUser(request):    
    if(request.method=='POST'):
        customer = User()
        customer.first_name=request.POST['first_name']
        customer.last_name=request.POST['last_name']
        customer.email=request.POST['email']
        customer.contact_no=request.POST['contact_no']
        customer.save()
        return redirect('/?success')
    else:
        return render(request,'register.html')

def loginUser(request):
    pass