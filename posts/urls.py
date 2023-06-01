from django.urls import path
from .views import Showposts,Tagsposts,Detailposts, deleted


urlpatterns = [
     path("", Showposts.as_view(), name="home"),
     path("tags/<slug:tag_slug>", Tagsposts.as_view(), name="posts_by_tag"),
     path("posts/<int:pk>", Detailposts.as_view(), name="postinfo"),
     path('deleted', deleted, name='deleted')
]
