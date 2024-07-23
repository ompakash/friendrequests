from django.urls import path
from .views import Message

urlpatterns = [
    path('message/', Message.as_view(), name='message'),  
]
