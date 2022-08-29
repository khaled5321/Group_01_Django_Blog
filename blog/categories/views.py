from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category
from django.core.mail import EmailMessage
# Create your views here.

def show_category(request, pk):
    pass

def subscribe(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "You have to login to subscribe!")
        # return redirect('home')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    cat=Category.objects.get(pk=pk)
    sub_cats= request.user.subscribed_categories.all()
    if cat in sub_cats:
        request.user.subscribed_categories.remove(cat)
        messages.success(request, "Unsubscribed Successfully!")
        msg=f"Hello {request.user.username} you have unsubscribed successfully in {cat.name}"
        # email = EmailMessage('Subject', msg, to=[request.user.email])
        # email.send()

    else:
        request.user.subscribed_categories.add(cat)
        messages.success(request, "Subscribed Successfully!")
        msg=f"Hello {request.user.username} you have subscribed successfully in {cat.name} welcome  aboard"
        # email = EmailMessage('Subject', msg, to=[request.user.email])
        # email.send()

    
    return redirect(request.META.get('HTTP_REFERER', '/'))

       