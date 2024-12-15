from django.db import models
from authen.models import User

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_body = models.TextField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to="post_images/", null=True, blank=False)
    post_likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    post_bookmarks = models.ManyToManyField(User, related_name='post_bookmarks', blank=True)

    def count_likes(self):
        return self.post_likes.count()
    
    def count_bookmarks(self):
        return self.post_bookmarks.count()

    def __str__(self):
        return self.post_body



class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def count_comments(self):
        return Comment.objects.filter(post=self.post).count()
