from django.contrib import admin
from.models import Post
from.models import Comment,Reply, BadWord

admin.site.register(BadWord)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','_tags']
    save_as = True
    def _tags(self,obj):
        return ", ".join(ob for ob in obj.tags.names())
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['user','content', 'created_at']
    
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display=['user','content','created_at']
  