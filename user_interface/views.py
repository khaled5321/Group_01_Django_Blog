from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.core.validators import validate_email
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from .forms import LoginForm
from .models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.POST:
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a correct email address!")
            return redirect('register')
        
        try:
            validator=ASCIIUsernameValidator()
            validator(user_name)
        except:
            messages.error(request, ASCIIUsernameValidator.message)
            return redirect('register')
        
        if User.get_object_or_none(username=user_name):
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.get_object_or_none(email=email):
            messages.error(request, 'Email already exists!')
            return redirect('register')

        if password!=confirm_password:
            messages.error(request, "Passwords don't match!")
            return redirect('register')

        user=User.objects.create(username=user_name, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Account Created successfully!')
        return redirect('login')
    
    else:
        return render(request, 'user_interface/registeration.html')
             

def login_view(request):
    form=LoginForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            if User.get_object_or_none(username=username):
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_blocked:
                        messages.error(request, 'Your account is locked, please contact an admin')
                        return render(request, 'user_interface/login.html', {'form':form})

                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Username OR password is not correct')      
            else:
                messages.error(request, 'There is no account with this username')
        else:
            messages.error(request, 'Please Enter valid inputs!')


    return render(request, 'user_interface/login.html', {'form':form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def block_user(request, pk):
    user=User.objects.get(pk=pk)
    if user.is_blocked:
        user.is_blocked=False
        user.save()
    else:
        user.is_blocked=True
        user.save()
    return redirect('show-users')


def promote_user(request, pk):
    user=User.objects.get(pk=pk)
    if user.is_superuser:
        user.is_superuser=False
        user.save()
    else:
        user.is_superuser=True
        user.save()
    return redirect('show-users')
