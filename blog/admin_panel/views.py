from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import ListView
from admin_panel.forms import PostsModelForm,CategoryModelForm,BadwordModelForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from user_interface.models import User
from categories.models import Category
from posts.models import Post,BadWord


class Createposts(CreateView):
    form_class = PostsModelForm
    template_name = "admin_panel/createpost.html"
    success_url = "/admin_panel/index"

class Deleteposts(DeleteView):
    
    model = Post
    success_url ="/admin_panel/index" 
    template_name = "admin_panel/deletepost.html"


class Updateposts(UpdateView):
    model = Post 
    fields = "__all__"  
    template_name = 'admin_panel/createpost.html' 
    success_url="/admin_panel/index" 


class Showposts(ListView):
    model=Post 
    template_name="admin_panel/createpost.html"
    
# categories view :


class Createcategory(CreateView):
    form_class = CategoryModelForm
    template_name = "admin_panel/createcategory.html"
    success_url = "/admin_panel/index"


class Deletecategory(DeleteView):
    
    model = Category
    success_url ="/admin_panel/index" 
    template_name = "admin_panel/deletecategory.html"

class Updatecategory(UpdateView):
    model = Category
    fields = "__all__"  
    template_name = 'admin_panel/createcategory.html' 
    success_url="/admin_panel/index" 

class Showcategory(ListView):
    model=Category
    template_name="admin_panel/createcategory.html"

    def get_context_data(self,*args,**kwargs):
        context = super(Showcategory,self).get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['category'] = category
        context['title']=category.name
        return context

# comments BAD WORD

class Createbadword(CreateView):
    form_class = BadwordModelForm
    template_name = "admin_panel/createbadword.html"
    success_url = "/admin_panel/index"

class Deletebadword(DeleteView):
    
    model = BadWord
    success_url ="/admin_panel/index" 
    template_name = "admin_panel/deletebadword.html"

class Updatebadword(UpdateView):
    model = BadWord
    fields = "__all__"  
    template_name = 'admin_panel/createbadword.html' 
    success_url="/admin_panel/index" 
    

class Showbadword(ListView):
    model=BadWord
    template_name="admin_panel/createbadword.html"
    