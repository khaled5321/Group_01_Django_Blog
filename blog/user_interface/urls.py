from django.urls import path
from .views import login_view, register, logoutUser

urlpatterns = [
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logoutUser, name="logout"),
]