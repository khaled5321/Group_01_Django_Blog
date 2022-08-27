from django.db import models
from taggit.managers import TaggableManager  # there is error regards to this line and its package
from django.shortcuts import get_object_or_404
# from categories.models import Category
from user_interface.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.CharField(null=True, max_length=100)
    tags = TaggableManager()
    image=models.ImageField(upload_to="posts/images/",null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    edited_at=models.DateTimeField(auto_now=True)
    
    # category_id=models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,related_name='cat_lib')
    user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,related_name='user_post')
    
    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return f"/media/{self.image}"
    def delete_url(self):
        return reverse("deleteposts",args=[self.id])
    
    @classmethod
    def get_all_object(cls):
        return cls.objects.all()
    
    def show_url(self):
        return reverse("",args=[self.id])
    
    def get_all_url(self):
        return reverse("postIndex")