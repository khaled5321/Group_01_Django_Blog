from pyexpat import model
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from categories.models import Category
from .models import Post
from django.views.generic import ListView,DetailView
from posts.forms import PostsModelForm,CommentsModelForm,ReplyModelForm
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator, EmptyPage


# def catsinfo(request,cats):
    
    
#     context = {"cats": cats}
   
#     return render(request, "posts/main.html", context)    

def get_cats(request,cats):    
    category_posts = Post.objects.filter(category_id=cats)
    return render(request, "posts/categories.html", {"cats":cats,"category_posts":category_posts}  )

# category - menu probl

# def catsinfo(request,category_id):
#     # category=Category.objects.get(pk=book_id)
#     category=Category.get_specific_object(category_id)
#     context = {"category": category}
   
#     return render(request, "posts/categories.html", context)  

class Detailposts(DetailView):
    model=Post
    template_name = "posts/post.html"
    
    #passing number of likes by context
    def get_context_data(self,*args,**kwargs):
        context = super(Detailposts,self).get_context_data(*args,**kwargs)
        clickable_post=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=clickable_post.total_likes()
        liked=False
        if clickable_post.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context['total_likes'] = total_likes
        context['liked'] = liked
        
        
        return context

 # for comment form and heading back to same page:
 
class Createposts(CreateView):
    form_class = CommentsModelForm
    template_name = "posts/create.html"

   
    def get_success_url(self):
        return reverse_lazy('postinfo', kwargs={'pk': self.object.post.pk})
    
    
        
        
   
class Showcomments(DetailView):
    model=Post
    
    template_name = "posts/post.html"
    
    #passing number of likes by context
    def get_context_data(self,*args,**kwargs):
        context = super(Createposts,self).get_context_data(*args,**kwargs)
       
        # comments=Comment.objects.all()
        fool_lang=['bad','stuipd','dumb','boo']
        # allcomments=[]
        # for comment in comments:
        #     for fool in fool_lang:
        #         if fool in comment['body']:
        #             comment['body']=comment['body'].replace(fool,'*****')
        #             allcomments.append(comment)
        #         else:
        #             allcomments.append(comment)
        context['fool_lang']=fool_lang
       
        return context
       




# for reply form and heading back to same page:

class Createreplies(CreateView):
    form_class = ReplyModelForm
    template_name = "posts/create.html"
   
    def get_success_url(self):
        return reverse_lazy('postinfo', kwargs={'pk': self.object.reply_post.pk})
    
    
class Showposts(ListView):
    
    model=Post
    template_name="posts/main.html"
    queryset=Post.objects.all()
    context_object_name='posts' 
    ordering=['-likes','-created_at']
    paginate_by = 2
   
    def get_context_data(self,*args,**kwargs):
        
        context = super(Showposts,self).get_context_data(*args,**kwargs)
        # passing cat_menu
        cat_menu=Category.objects.all()
        context['cat_menu'] = cat_menu
        return context



    

#     return render(request, "posts/postinfo.html", {})
    
   
      
    

class Tagsposts(ListView):
    model=Post
    template_name="posts/main.html"
    queryset=Post.objects.all()
    context_object_name='posts'  
    # this method is used to return the associated posts related to same tags
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')) 
    
    
    
def likeview(request,post_id):
    post= get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('postinfo',args=[str(post_id)]))


    
def top_rated_posts(request, page=1):
    
    q=Post.objects.filter().order_by('-created_at','-likes')
    paginator = Paginator(q,5)
    try:
        q = paginator.page(page)
    except EmptyPage:
       
        q = paginator.page(paginator.num_pages)
    context = {"top_posts": q}
    return render(request, "posts/top_posts.html", context  )
