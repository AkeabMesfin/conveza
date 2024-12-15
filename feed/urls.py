from django.urls import path, include
from . import views
urlpatterns = [
    path('feed', views.feed, name='feed'),
    path('feed/like/<int:post_id>', views.like, name='like'),
    path('feed/bookmark/<int:post_id>', views.bookmark, name='bookmark'),
    path('feed/comments/<int:post_id>/', views.comments, name='comments'),
    path('feed/create-post', views.create_post, name='create-post'),
]
