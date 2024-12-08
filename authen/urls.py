from django.urls import path, include
from . import views
urlpatterns = [
    path('sign-up', views.sign_up, name='sign-up'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
