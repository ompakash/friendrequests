from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from accounts.models import CustomUser
from .serializers import UserSerializer

class Message(APIView):
    def get(self, request):
        return Response({"message": "You are authenticated into core api!"}, status=status.HTTP_200_OK)

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
