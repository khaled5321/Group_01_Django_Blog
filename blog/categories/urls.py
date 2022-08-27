from django.urls import path
from .views import show_category, subscribe

urlpatterns = [
    path("category/<int:pk>", show_category, name="show_category"),
    path("subscribe/<int:pk>", subscribe, name="subscribe"),
]