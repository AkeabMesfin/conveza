from django.urls import path, include
from . import views
import uuid
urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('chat/create-group/', views.create_group, name='create-group'),
    path('chat/group/<uuid:group_id>/', views.group_chat, name='group-chat'),
    path('chat/group/<uuid:group_id>/detail/', views.group_detail, name='group-detail'),
    path('chat/group/<uuid:group_id>/detail/leave/', views.leave_group, name='leave-group'),
    path('chat/group/<uuid:group_id>/join/', views.join_group, name='join-group'),
    path('chat/private/<uuid:room_id>/', views.private_chat, name='private-chat'),
]
