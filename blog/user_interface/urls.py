from django.urls import path
from .views import login_view, register, logoutUser, block_user, promote_user

urlpatterns = [
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logoutUser, name="logout"),
    path("block/<int:pk>", block_user, name="block_user"),
    path("promote/<int:pk>", promote_user, name="promote_user"),
]