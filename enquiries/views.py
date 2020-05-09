from django.shortcuts import render
from django.http import request,response,HttpResponse
from customers.models import Customer
# Create your views here.

def index(request):
    return render(request,'index.html',{
        'name':'AMS',
        'latest_customers':Customer.objects.all(),       
        

    })

def about(request):
    return HttpResponse('<h1>About Us</h1>')
