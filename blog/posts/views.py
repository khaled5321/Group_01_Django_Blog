from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from categories.models import Category
from .models import Post, Comment, Reply, BadWord


def check_for_bad_words(str):
    bad_words=BadWord.objects.all()

    for bad_word in bad_words:
        if bad_word.word in str:
            str=str.replace(bad_word.word,len(bad_word.word)*'*')
    
    return str


class Detailposts(DetailView):
    model=Post
    template_name = "posts/post.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            messages.error(request, 'You have to login first!')
            return redirect('login')

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
            
            elif not self.object.dislikes.filter(id=request.user.id).exists():
                self.object.dislikes.add(request.user)
            
            if self.object.dislikes.count() == 10:
                self.object.delete()
                return redirect('deleted')

        elif option == 'comment':
            content = self.request.POST.get('comment')
            content = check_for_bad_words(content)
            Comment.objects.create(content=content, post=self.object, user=request.user)


        elif option == 'reply':
            content = self.request.POST.get('content')
            content = check_for_bad_words(content)
            comment_id = self.request.POST.get('comment_id')
            comment= Comment.objects.get(id=comment_id)
            Reply.objects.create(
                reply_post=self.object, 
                comment=comment, 
                user=request.user,
                content=content,
                )

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
        context['title'] = self.kwargs.get('tag_slug')
        return context

    # this method is used to return the associated posts related to same tags
    def get_queryset(self):
        object_list = Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')) 
        return object_list

def deleted(request):
    return render(request,'posts/deleted.html')
