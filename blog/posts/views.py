from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from categories.models import Category
from .models import Post, Comment, Reply, BadWord


class Detailposts(DetailView):
    model=Post
    template_name = "posts/post.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        option=self.request.POST.get('option')
        if option == 'like':
            if self.object.likes.filter(id=request.user.id).exists():
                self.object.likes.remove(request.user)
            else:
                self.object.likes.add(request.user)
        elif option == 'dislike':
            if self.object.likes.filter(id=request.user.id).exists():
                self.object.likes.remove(request.user)
                self.object.dislikes.add(request.user)

            elif self.object.dislikes.filter(id=request.user.id).exists():
                self.object.dislikes.remove(request.user)

        return redirect('postinfo',self.object.id)

    def get_object(self):
        object = get_object_or_404(Post,id=self.kwargs['pk'])
        return object

    #passing number of likes by context
    def get_context_data(self,*args,**kwargs):
        context = super(Detailposts,self).get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        object=self.get_object()
        liked=False
        disliked= False
        if object.likes.filter(id=self.request.user.id).exists():
            liked=True
        if object.dislikes.filter(id=self.request.user.id).exists():
            disliked=True
        
        context['liked'] = liked
        context['disliked'] = disliked
        
        return context

   
# class Showcomments(DetailView):
#     model=Post
    
#     template_name = "posts/post.html"
    
#     #passing number of likes by context
#     def get_context_data(self,*args,**kwargs):
#         context = super(Createposts,self).get_context_data(*args,**kwargs)
       
#         # comments=Comment.objects.all()
#         fool_lang=['bad','stuipd','dumb','boo']
#         # allcomments=[]
#         # for comment in comments:
#         #     for fool in fool_lang:
#         #         if fool in comment['body']:
#         #             comment['body']=comment['body'].replace(fool,'*****')
#         #             allcomments.append(comment)
#         #         else:
#         #             allcomments.append(comment)
#         context['fool_lang']=fool_lang
       
#         return context
       


# class Createreplies(CreateView):
#     # form_class = ReplyModelForm
#     template_name = "posts/create.html"
   
#     def get_success_url(self):
#         return reverse_lazy('postinfo', kwargs={'pk': self.object.reply_post.pk})
    
    
class Showposts(ListView):
    model=Post
    template_name="posts/home.html"
    paginate_by = 5

    def get_context_data(self,*args,**kwargs):
        context = super(Showposts,self).get_context_data(*args,**kwargs)
        # passing cat_menu
        context['categories'] = Category.objects.all()
        context['title'] = 'Top Posts'
        return context
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = self.model.objects.all()

        if q:
            object_list = self.model.objects.filter(Q(title__icontains=q) | Q(tags__name__icontains=q))

        return object_list    



class Tagsposts(ListView):
    model=Post
    template_name="posts/home.html"
    queryset=Post.objects.all()

    def get_context_data(self,*args,**kwargs):
        context = super(Tagsposts,self).get_context_data(*args,**kwargs)
        # passing cat_menu
        context['categories'] = Category.objects.all()
        context['tilte'] = self.kwargs.get('tag_slug')
        return context

    # this method is used to return the associated posts related to same tags
    def get_queryset(self):
        object_list = Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')) 
        return object_list
