from django.contrib import admin
from . models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'created_at', 'has_image', 'comment_count', 'like_count', 'bookmark_count']
    list_filter = ['post_id', 'user', 'created_at']

    def get_username(self, obj):
        return obj.user.username if obj.user else 'No user assigned'
    get_username.short_description = 'Username'

    def has_image(self, obj):
        return 'Yes' if obj.post_image else 'No'
    
    def comment_count(self, obj):
         return obj.comments.count()  # Use 'comments' instead of 'comment_set'
    comment_count.short_description = 'Number of Comments'  # Optional: Set a custom header

    def like_count(self, obj):
        return obj.post_likes.count()
    like_count.short_description = 'Likes'
    def bookmark_count(self, obj):
        return obj.post_bookmarks.count()
    bookmark_count.short_description = 'Bookmarks'

# Register the model and admin class
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'get_post_id']
    list_filter = ['post__post_id', 'user'] 
    

    def get_username(self, obj):
        return obj.user.username if obj.user else 'No user assigned'
    get_username.short_description = 'Username'

    def get_post_id(self, obj):
        return obj.post.post_id  # Access post_id from the related Post model
    get_post_id.short_description = 'Post ID'


admin.site.register(Comment, CommentAdmin)