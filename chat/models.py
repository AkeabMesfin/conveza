import uuid
from django.db import models
from authen.models import User

class PrivateChat(models.Model):
    room_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="private_chats_initiated")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="private_chats_received")
    created_at = models.DateTimeField(auto_now_add=True)

class PrivateMessage(models.Model):
    chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class GroupChat(models.Model):
    group_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  
    group_name = models.CharField(max_length=50, blank=False) 
    group_username = models.CharField(max_length=10, unique=True) 
    description = models.TextField(blank=False, null=True) 
    group_photo = models.ImageField(upload_to="group_photos/", blank=False, null=True)  
    members = models.ManyToManyField(User, related_name="members")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

    def count_members(self):
        return self.members.count()

class GroupMessage(models.Model):
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
