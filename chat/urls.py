from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/chat/stream', views.chat, name='chat_stream'),  # Endpoint for SSE
]