from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views.generic import ListView
from posts.forms import PostsModelForm
from django.views.generic.edit import CreateView


def deletepost(request,post_id):
    deleted_post=Post.objects.get(pk=post_id)
    url=deleted_post.get_all_url()
    deleted_post.delete()
    return HttpResponseRedirect(url)

class Createposts(CreateView):
    form_class = PostsModelForm
    template_name = "posts/create.html"
# class will send object form to the template
    success_url = "/posts/index"
    
class Showposts(ListView):
    model=Post
    template_name="posts/main.html"
      
    

class Tagsposts(ListView):
    model=Post
    template_name="posts/main.html"
    queryset=Post.objects.all()
    context_object_name='posts'  
    # this method is used to return the associated posts related to same tags
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')) 
    
    
    
    

