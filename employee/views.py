from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Person
# Create your views here.

def home(request):
    return render(request,'index.html')

def index(request):
    if request.method == 'POST':        
        data = request.POST 
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']   
        
        obj = Person.objects.create(first_name=first_name,
                                    last_name=last_name,
                                    email= email)
        if obj:
            return redirect('/employee')
        return HttpResponse('Employee is not created ')   
        
    else:
        persons = Person.objects.all()        
        context = {
            'persons': persons
        }
    return render(request,'employee/index.html',context)

def add(request):
    return HttpResponse("<h1>Add Employee</h1>")

def edit(request,id):
    person = Person.objects.get(id=id) 
    if request.method == 'POST':
        person.first_name =request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.email = request.POST['email']
        person.save()
        return redirect('/employee')
    context ={
        'person':person
    }
    return render(request,'employee/edit.html',context)

def delete(request,id):    
    person = Person.objects.get(id=id)
    person.delete()
    
    return redirect('/employee')
