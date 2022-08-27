
from django import forms
from .models import Post

class PostsModelForm (forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"