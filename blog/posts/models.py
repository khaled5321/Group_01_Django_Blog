from django.db import models
from taggit.managers import TaggableManager  # there is error regards to this line and its package, you should pip install django-taggit
from django.shortcuts import get_object_or_404
from categories.models import Category
from user_interface.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.CharField(null=True, max_length=1000)
    tags = TaggableManager()
    image=models.ImageField(upload_to="posts/images/",null=True)
    created_at=models.DateTimeField(default=timezone.now,null=True)
    edited_at=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User ,related_name='blog_post')
    category_id=models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,related_name='cat_post')
    user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,related_name='user_post')
    # comment=
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
   
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
        return reverse("postIndex")
    
    
    
    
class Comment(models.Model):
    post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='comment_post')
    name=models.CharField(max_length=240)
    body=models.TextField()
    created_at=models.DateTimeField(default=timezone.now,null=True)
    

    
    

    def __str__(self):
        return'%s - %s'%(self.post,self.name)
   
   
class Reply(models.Model):
    
    reply_post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='re_post')
    reply_name=models.CharField(max_length=240)
    reply_body=models.TextField()
    reply_created_at=models.DateTimeField(default=timezone.now,null=True)
    reply=models.ForeignKey('Comment' ,null=True,related_name='replies',on_delete=models.CASCADE)
    
    def __str__(self):
        return'%s - %s'%(self.reply_post,self.reply_name)
    