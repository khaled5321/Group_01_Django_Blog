from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.urls import reverse

class UserAdmin(admin.ModelAdmin):
    list_display = ['users', 'block_user', 'promote_to_admin']
    search_fields=['username']
    fields = ['username', 'email', 'password', 'subscribed_categories']
    filter_horizontal = ('subscribed_categories',)

    def users(self, obj):
        if obj.is_superuser:
            return format_html(f'<div style="width:100%%; height:100%%; background-color:red;">{obj.username}</div>')

        return obj.username

    def block_user(self, obj):
        link = reverse("block_user")
        if not obj.is_superuser:
            if not obj.is_blocked:
                return format_html('''<a href="{0}?q=block&id={1}">Block</a>''',link,obj.id)
            else:
                return format_html('''<a href="{0}?q=unblock&id={1}" style="color:yellow;">Unblock</a>''',link,obj.id)
    
    def promote_to_admin(self, obj):
        link = reverse("promote_user")
        if not obj.is_superuser and  not obj.is_blocked:
            return format_html('''<a href="{0}?q=promote&id={1}">Promote</a>''',link,obj.id)



admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.site_header="Admin Page"
admin.site.site_title = "Admin"