from django.shortcuts import render
from django.views.generic import ListView
from admin_panel.forms import PostsModelForm,CategoryModelForm,BadwordModelForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from user_interface.models import User
from categories.models import Category
from posts.models import Post, BadWord


class Createposts(CreateView):
    form_class = PostsModelForm
    template_name = "admin_panel/createpost.html"
    success_url = "../showPost"

class Deleteposts(DeleteView):
    model = Post
    template_name = "admin_panel/deletepost.html"
    success_url = "../showPost" 


class Updateposts(UpdateView):
    model = Post 
    form_class= PostsModelForm
    template_name = 'admin_panel/createpost.html' 
    success_url = "../showPost"


class Showposts(ListView):
    model=Post 
    template_name="admin_panel/showposts.html"
    

# categories view :
class Createcategory(CreateView):
    form_class = CategoryModelForm
    template_name = "admin_panel/createcategory.html"
    success_url = "showCategory"


class Deletecategory(DeleteView):
    model = Category
    template_name = "admin_panel/deletecategory.html"
    success_url ='../showCategory' 

class Updatecategory(UpdateView):
    model = Category
    fields = "__all__"  
    template_name = 'admin_panel/createcategory.html' 
    success_url ='../showCategory' 

class Showcategory(ListView):
    model=Category
    template_name="admin_panel/showcategory.html"


# comments BAD WORD
class Createbadword(CreateView):
    form_class = BadwordModelForm
    template_name = "admin_panel/createbadword.html"
    success_url ="index" 


class Deletebadword(DeleteView):
    model = BadWord
    template_name = "admin_panel/deletebadword.html"
    success_url ="index" 

class Updatebadword(UpdateView):
    model = BadWord
    fields = "__all__"  
    template_name = 'admin_panel/createbadword.html' 
    success_url ="index" 
    

class Showbadword(ListView):
    model=BadWord
    template_name="admin_panel/createbadword.html"
    
@staff_member_required    
def dashboardIndex(request):
    posts=Post.get_all_object()
    badwords=BadWord.get_all_object()
    context = {"allposts": posts,"allbadwords":badwords}
    return render(request, "admin_panel/main.html", context)
