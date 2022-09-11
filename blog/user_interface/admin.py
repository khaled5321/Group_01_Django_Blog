from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.unregister(Group)

admin.site.site_header="Admin Page"
admin.site.site_title = "Admin"