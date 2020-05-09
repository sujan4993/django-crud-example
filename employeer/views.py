from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import EmployeerForm
from .models import Employeer
# Create your views here.


def index(request):
   
    context = {
        'employeers':Employeer.objects.all()
    }    
    return render(request, 'employeer/index.html',context)

def create(request):
    if request.method == 'POST':
        form = EmployeerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employeer')
     
    context = {
        'form':EmployeerForm()
    }
    return render(request,'employeer/create.html',context)

def edit(request,id):
    instance=Employeer.objects.get(id = id)
    if request.method == 'POST':
        form = EmployeerForm(request.POST,instance= instance)
        if form.is_valid():
            form.save()
            return redirect('/employeer')

     
    context = {
        
        'form':EmployeerForm(instance=instance)
    }
    return render(request,'employeer/create.html',context)
 
def delete(request,id):
    instance=Employeer.objects.get(id = id)
    instance.delete()
    return redirect('/employeer')