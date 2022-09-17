from django.urls import re_path

from app01 import consumers

websocket_urlpatterns = [
    re_path(r"^app/room/(?P<group>\w+)&(?P<id>\w+)/$", consumers.ChatConsumer.as_asgi()),
]

