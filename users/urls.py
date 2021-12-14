from .views import lazy_load_users
from django.urls import path

urlpatterns = [
    path('lazy_load_users/', lazy_load_users, name='lazy_load_users'),
]
