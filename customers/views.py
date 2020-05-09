from django.shortcuts import render,HttpResponse,redirect
from .models import Customer
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin/login')
def register(request):
    if(request.method=='POST'):
        customer = Customer()
        customer.first_name=request.POST['first_name']
        customer.last_name=request.POST['last_name']
        customer.email=request.POST['email']
        customer.contact_no=request.POST['contact_no']
        customer.save()
        return redirect('/?success')
    else:
        return render(request,'register.html')