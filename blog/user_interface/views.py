from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import User

def register(request):
    if request.POST:
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

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
        # return redirect('home')
        return HttpResponse('Home')

    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            
            if User.get_object_or_none(email=email):
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    # return redirect('home')
                    return HttpResponse('Home')
                else:
                    messages.error(request, 'Email OR password is not correct')      
            else:
                messages.error(request, 'This Email is not registered!')
        else:
            messages.error(request, 'Please Enter valid inputs!')


    return render(request, 'user_interface/login.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('home')
