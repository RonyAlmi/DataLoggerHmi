from django.urls import path
from .consumers import HmiConsumer

ws_urlpatterns = [
    path('ws/demohmi/', HmiConsumer.as_asgi())
]