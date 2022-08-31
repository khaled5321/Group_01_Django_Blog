from django.urls import path
from .views import show_category, subscribe, SubscribedCategories

urlpatterns = [
    path("category/<int:pk>", show_category, name="show_category"),
    path("subscribe/<int:pk>", subscribe, name="subscribe"),
    path("subscribed_cats/", SubscribedCategories.as_view(), name="subscribed_cats"),
]