from django.urls import path
from .views import login_view, register, logoutUser, block_user, promote_user, home, post_details

urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logoutUser, name="logout"),
    path("block", block_user, name="block_user"),
    path("promote", promote_user, name="promote_user"),
    path("post", post_details, name="post_details"),

]