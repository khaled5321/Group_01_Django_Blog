from django import forms
from posts.models import Post,Comment,Reply,BadWord
from categories.models import Category
from user_interface.models import User


class PostsModelForm (forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        exclude= ['likes', 'dislikes']
            

class CategoryModelForm (forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
        
        
class UserModelForm (forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        
        
class BadwordModelForm(forms.ModelForm):
    class Meta:
        model=BadWord
        fields="__all__"