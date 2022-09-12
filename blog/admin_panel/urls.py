from django.urls import path
from . import  views


urlpatterns = [
     path("index", views.dashboardIndex, name="dashIndex"),

#    Post urls
     path("createPost", views.Createposts.as_view(), name="create-post"),
     path("updatePost/<int:pk>", views.Updateposts.as_view(), name="update-post"),
     path("deletePost/<int:pk>", views.Deleteposts.as_view(), name="delete-post"),
     path("showPost/", views.Showposts.as_view(), name="show-post"),

#    Category urls 
     path("createCategory", views.Createcategory.as_view(), name="create-category"),
     path("updateCategory/<int:pk>", views.Updatecategory.as_view(), name="update-category"),
     path("deleteCategory/<int:pk>", views.Deletecategory.as_view(), name="delete-category"),
     path("showCategory/", views.Showcategory.as_view(), name="show-category"),

#    Badword urls
     path("createBadword", views.Createbadword.as_view(), name="create-badword"),
     path("updateBadword/<int:pk>", views.Updatebadword.as_view(), name="update-badword"),
     path("deleteBadword/<int:pk>", views.Deletebadword.as_view(), name="delete-badword"),
     path("showBadword/", views.Showbadword.as_view(), name="show-badword"),

     #users
     path('users/', views.ShowUsers.as_view(),name="show-users")
    
]
