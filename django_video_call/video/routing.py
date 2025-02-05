from django.urls import path
from .consumers import VideoChatConsumer

websocket_urlpatterns = [
    path("ws/videochat/", VideoChatConsumer.as_asgi()),
]
