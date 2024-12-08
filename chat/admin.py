from django.contrib import admin
from .models import GroupChat, PrivateChat, PrivateMessage, GroupMessage

admin.site.register(GroupChat)
admin.site.register(PrivateChat)
admin.site.register(PrivateMessage)
admin.site.register(GroupMessage)