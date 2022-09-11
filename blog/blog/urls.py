from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user_interface.urls")),
    path("", include("categories.urls")),
    path("", include("posts.urls")),
    path("", include("admin_panel.urls")),
]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
