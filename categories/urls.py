from django.urls import path
from .views import ShowCategory, subscribe, SubscribedCategories

urlpatterns = [
    path("category/<int:pk>", ShowCategory.as_view(), name="show_category"),
    path("subscribe/<int:pk>", subscribe, name="subscribe"),
    path("subscribed_cats/", SubscribedCategories.as_view(), name="subscribed_cats"),
]