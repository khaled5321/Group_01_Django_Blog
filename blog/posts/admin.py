from django.contrib import admin

from.models import Post
from.models import Comment,Reply
# admin.site.register(Post),ReplyComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','get_tags']
    
    def get_tags(self,obj):
        return ",".join(ob for ob in obj.tags.names())
    

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display=['name','post']
    
@admin.register(Reply)
class PostAdmin(admin.ModelAdmin):
    list_display=['reply_name','reply_post','reply']
  