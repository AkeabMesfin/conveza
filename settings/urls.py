from django.urls import path
from . import views

urlpatterns = [
    path('settings', views.settings, name='settings'),
    path('settings/liked-saved-posts', views.liked_saved_post, name='liked-saved-posts')
]