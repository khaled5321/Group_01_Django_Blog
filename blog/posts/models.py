from django.db import models
from taggit.managers import TaggableManager  
from django.shortcuts import get_object_or_404
from categories.models import Category
from user_interface.models import User
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField(null=True, max_length=5000)

    tags = TaggableManager()
    image=models.ImageField(upload_to="posts/images/",null=True)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    edited_at=models.DateTimeField(auto_now=True)

    likes=models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dislikes=models.ManyToManyField(User, related_name='blog_dislikes',  blank=True)

    category_id=models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,related_name='cat_posts')
    user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,related_name='user_posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return f"/media/{self.image}"
 
    @classmethod
    def get_all_object(cls):
        return cls.objects.all()
    
    @classmethod
    def get_specific_object(cls,id):
        return get_object_or_404(cls,pk=id)
    
    def show_url(self):
        return reverse("postinfo",args=[self.id])
    
    def get_all_url(self):
        return reverse("home")
    
    
class Comment(models.Model):
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_replies(self):
        return self.replies.all()
    
   
class Reply(models.Model):
    reply_post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='re_post')
    comment=models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username


class BadWord(models.Model):
    word=models.CharField(max_length=120, null=True)

    @classmethod
    def get_all_object(cls):
        return cls.objects.all()

    def __str__(self):
        return self.word
