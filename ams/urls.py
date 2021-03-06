"""ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from enquiries.views import index,about
from customers.views import register
# from employee.views import home
from .views import home,admin_index,registerUser,loginUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('administrator',admin_index),
    path('register/',registerUser),
    path('login',loginUser),
    path('employee/',include('employee.urls')),
    path('employeer/',include('employeer.urls')),
    path('accounts/',include('accounts.urls')),
    path('customer/',index),
    path('about/',about),
    # path('register/', register),
]
