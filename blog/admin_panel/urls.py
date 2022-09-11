
from django.urls import path
from admin_panel.views import  Updatebadword,dashboardIndex,Deletebadword,Createbadword,Deleteposts,Createposts,Updateposts,Createcategory,Deletecategory,Updatecategory
# ,Showbadword,Showcategory,Showposts
urlpatterns = [
   
    
    
     path("index", dashboardIndex, name="dashIndex"),

#      Post urls
     path("createPost", Createposts.as_view(), name="create-post"),
     path("updatePost/<int:pk>", Updateposts.as_view(), name="update-post"),
     path("deletePost/<int:pk>", Deleteposts.as_view(), name="delete-post"),
     # path("showPost/", Showposts.as_view(), name="show-post"),
#      Category urls 
     path("createCategory", Createcategory.as_view(), name="create-category"),
     path("updateCategory/<int:pk>", Updatecategory.as_view(), name="update-category"),
     path("deleteCategory/<int:pk>", Deletecategory.as_view(), name="delete-category"),
     # path("showCategory/", Showcategory.as_view(), name="show-category"),
#      Badword urls
     path("createBadword", Createbadword.as_view(), name="create-badword"),
     path("updateBadword/<int:pk>", Updatebadword.as_view(), name="update-badword"),
      path("deleteBadword/<int:pk>", Deletebadword.as_view(), name="delete-badword"),
     #  path("showBadword/", Showbadword.as_view(), name="show-badword"),
]
