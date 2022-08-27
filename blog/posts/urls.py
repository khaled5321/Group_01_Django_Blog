
from django.urls import path
from posts.views import Showposts, deletepost,Createposts,Tagsposts
# from .views import 
urlpatterns = [
   
     path("index", Showposts.as_view(), name="postIndex"),
     path("delete/<int:pk>", deletepost, name="deletepost"),
     path("createPost", Createposts.as_view(), name="create"),
     path("tags/<slug:tag_slug>", Tagsposts.as_view(), name="posts_by_tags"),
]
