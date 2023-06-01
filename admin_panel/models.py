from django.db import models
from user_interface.models import User
from categories.models import Category
from posts.models import Post
from django.urls import reverse


class Admin(models.Model):
    name=models.CharField(max_length=40)
    user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,related_name='user_admin')
    category_id=models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,related_name='admin_cat')
    post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='post_admin')
    
    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f"/media/{self.image}"
    
    @classmethod
    def get_all_object(cls):
        return cls.objects.all()
    
    def show_url(self):
        return reverse("",args=[self.id])
    
    def get_all_url(self):
        return reverse("adminIndex")