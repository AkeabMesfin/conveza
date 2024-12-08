from django.urls import path
from . import views

urlpatterns = [
    path('profile/<uuid:id>', views.user_profile, name='user-profile'),
    path('settings/my-profile', views.my_profile, name='my-profile'),
    path('chat/private/start/<uuid:id>/', views.start_private_chat, name='start-private-chat'),
]
