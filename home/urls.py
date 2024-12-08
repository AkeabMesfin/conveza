from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('term-conditions', views.term_conditions, name='term-conditions'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
]
