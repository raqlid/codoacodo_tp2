# users/urls.py
from django.urls import path
from .views import init_db

urlpatterns = [
    path('init_db/', init_db, name='init_db'),
]
