from email import message
from venv import create
from django.shortcuts import render

from django.shortcuts import redirect,render

from blog.user_interface.models import User
def register(request):
    if request.POST:
        First_name=request.POST['First_name']
        Last_name=request.POST['Last_name']
        User_name=request.POST['User_name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        
        confirm_password=request.POST['confirm_password']
        if Password==confirm_password:
            if User.objects.filter(User_name=User_name).existis():
                message.info(request,'Email is signed up before')
                return redirect(register)
         