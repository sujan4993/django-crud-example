from django.shortcuts import render,redirect
from employee.models import Person

def home(request):
    employee = Person.objects.all().count()
    context = {
        'employee':employee
    }
    return render(request,'home.html',context)

def admin_index(request):
    return render(request,'admin-index.html')
