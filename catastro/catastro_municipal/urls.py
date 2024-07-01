from django.urls import path
from .views import gestion_view

urlpatterns = [
    path('gestion/', gestion_view, name='gestion_view'),
]
