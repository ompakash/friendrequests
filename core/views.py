from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from accounts.models import CustomUser
from core.serializers import *

class UserSearchView(APIView):
    def get(self, request):
        email_search = request.query_params.get('email_search', '')
        name_search = request.query_params.get('name_search', '')
        print(email_search)
        print(name_search)
        if not email_search and not name_search:
            return Response({"error": "email_search or name_search is required"}, status=status.HTTP_400_BAD_REQUEST)

        if '@' in email_search:
            users = CustomUser.objects.filter(email__iexact=email_search)
        else:
            users = CustomUser.objects.filter(Q(full_name__icontains=name_search))

        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)


class SendFriendRequestView(APIView):
    def post(self, request, user_id):
        receiver = CustomUser.objects.get(id=user_id)
        sender = request.user

        if FriendRequest.objects.filter(sender=sender, receiver=receiver).exists():
            return Response({"error": "Friend request already sent"}, status=status.HTTP_400_BAD_REQUEST)

        friend_request = FriendRequest(sender=sender, receiver=receiver)
        friend_request.save()

        return Response({"message": "Friend request sent", "friend_request_id": friend_request.id}, status=status.HTTP_201_CREATED)

class RespondToFriendRequest(APIView):
    def post(self, request, request_id, action):
        friend_request = FriendRequest.objects.get(id=request_id, receiver=request.user)
        if action == "accept":
            friend_request.is_accepted = True
            friend_request.save()
            return Response({"message": "Friend request accepted"}, status=status.HTTP_200_OK)
        elif action == "reject":
            friend_request.delete()
            return Response({"message": "Friend request rejected"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


class ListFriendsView(APIView):

    def get(self, request):
        user = request.user
        friends = CustomUser.objects.filter(
            received_friend_requests__sender=user,
            received_friend_requests__is_accepted=True
        ) | CustomUser.objects.filter(
            sent_friend_requests__receiver=user,
            sent_friend_requests__is_accepted=True
        )
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListPendingFriendRequestsView(APIView):

    def get(self, request):
        user = request.user
        pending_requests = FriendRequest.objects.filter(receiver=user, is_accepted=False)
        serializer = FriendRequestSerializer(pending_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
