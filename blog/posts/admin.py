from django.contrib import admin

from.models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','get_tags','content']
    
    def get_tags(self,obj):
        return ",".join(ob for ob in obj.tags.names())