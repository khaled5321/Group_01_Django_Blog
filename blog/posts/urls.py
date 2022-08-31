from django.urls import path
from .views import Showposts,Showcomments,Tagsposts,likeview,Detailposts


urlpatterns = [
     path("", Showposts.as_view(), name="home"),
     path("tags/<slug:tag_slug>", Tagsposts.as_view(), name="posts_by_tag"),
     path("posts/<int:pk>", Detailposts.as_view(), name="postinfo"),
     path("like/<post_id>", likeview, name="like_post"),
     path("specificomment/<int:pk>", Showcomments.as_view(), name="fool"),
]
