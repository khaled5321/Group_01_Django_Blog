from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import ListView
from django.db.models import Q
from .models import Category
from posts.models import Post


class ShowCategory(ListView):
    model=Post
    template_name="posts/home.html"
    paginate_by = 5

    def get_context_data(self,*args,**kwargs):
        context = super(ShowCategory,self).get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['category'] = category
        context['title']=category.name
        return context
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        category = Category.objects.get(pk=self.kwargs['pk'])
        object_list = category.cat_posts.all()

        if q:
            object_list = self.model.objects.filter(Q(title__icontains=q) | Q(tags__name__icontains=q))
        return object_list


    
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


class SubscribedCategories(ListView):
    model=Post
    template_name="posts/home.html"
    paginate_by = 5
    
    def get(self, *args, **kwargs):
        if not self.request.user.subscribed_categories.all():
            return redirect('home')
        return super(SubscribedCategories, self).get(*args, **kwargs)

    def get_context_data(self,*args,**kwargs):
        context = super(SubscribedCategories,self).get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        context['title']='Subscribed Categories'
        return context
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        subscribed_categories= self.request.user.subscribed_categories.all()
        object_list = self.model.objects.all()

        if subscribed_categories:
            object_list= self.model.objects.none()
            for cat in subscribed_categories:
                objectlist = self.model.objects.filter(category_id=cat)
                object_list = objectlist |object_list 
    
        if q:
            object_list = self.model.objects.filter(Q(title__icontains=q) | Q(tags__name__icontains=q))

        return object_list