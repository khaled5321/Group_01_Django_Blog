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
    success_url = "../index"

class Deleteposts(DeleteView):
    
    model = Post
    success_url ="../index" 
    template_name = "admin_panel/deletepost.html"


class Updateposts(UpdateView):
    model = Post 
    fields = "__all__"  
    template_name = 'admin_panel/createpost.html' 
    success_url="../index" 


# class Showposts(ListView):
#     model=Post 
#     template_name="admin_panel/createpost.html"
    
# categories view :


class Createcategory(CreateView):
    form_class = CategoryModelForm
    template_name = "admin_panel/createcategory.html"
    success_url = "../index"


class Deletecategory(DeleteView):
    
    model = Category
    success_url ="../index" 
    template_name = "admin_panel/deletecategory.html"

class Updatecategory(UpdateView):
    model = Category
    fields = "__all__"  
    template_name = 'admin_panel/createcategory.html' 
    success_url="../index" 

# class Showcategory(ListView):
#     model=Category
#     template_name="admin_panel/createcategory.html"

   

# comments BAD WORD

class Createbadword(CreateView):
    form_class = BadwordModelForm
    template_name = "admin_panel/createbadword.html"
    success_url = "../index"

class Deletebadword(DeleteView):
    
    model = BadWord
    success_url ="../index" 
    template_name = "admin_panel/deletebadword.html"

class Updatebadword(UpdateView):
    model = BadWord
    fields = "__all__"  
    template_name = 'admin_panel/createbadword.html' 
    success_url="../index" 
    

# class Showbadword(ListView):
#     model=BadWord
#     template_name="admin_panel/createbadword.html"
    
    
def dashboardIndex(request):
  
    posts=Post.get_all_object()
    badwords=BadWord.get_all_object()
    categories=Category.get_all_object()
    context = {"allposts": posts,"allcategories":categories,"allbadwords":badwords}
    return render(request, "admin_panel/main.html", context)
