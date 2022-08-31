
from django.urls import path
# ,postsinfo
from posts.views import Showposts,Showcomments,Createposts,Tagsposts,top_rated_posts,likeview,Detailposts,get_cats,Createreplies
# from .views import ,catsinfo
urlpatterns = [
   
     path("index", Showposts.as_view(), name="postIndex"),
     path("createPost", Createposts.as_view(), name="create"),
     path("tags/<slug:tag_slug>", Tagsposts.as_view(), name="posts_by_tags"),
     path("specificpost/<int:pk>", Detailposts.as_view(), name="postinfo"),
     path("like/<post_id>", likeview, name="like_post"),
     # path("info/<str:category_id>", catsinfo, name="catinfo"),
     path("info/<str:cats>", get_cats, name="catinfo"),
     path("createReply", Createreplies.as_view(), name="createreply"),
     path("top", top_rated_posts  , name="topPosts"),
     path("specificomment/<int:pk>", Showcomments.as_view(), name="fool"),
    
   
]
