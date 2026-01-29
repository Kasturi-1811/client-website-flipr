from django.urls import path
from .views import subscribe

urlpatterns = [
    path('add/', subscribe, name='subscribe'),
]
