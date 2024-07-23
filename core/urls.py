from django.urls import path
from .views import *

urlpatterns = [
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/send/<int:user_id>/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/respond/<int:request_id>/<str:action>/', RespondToFriendRequest.as_view(), name='respond-friend-request'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('friend-requests/pending/', ListPendingFriendRequestsView.as_view(), name='list-pending-friend-requests'),
]
