from django.urls import path
from .views import *

urlpatterns = [
    path('message/', Message.as_view(), name='message'),  
    path('search/', UserSearchView.as_view(), name='user-search'),

]
