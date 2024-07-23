from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status

class Message(APIView):

    def get(self, request):
        return Response({"message": "You are authenticated into core api!"}, status=status.HTTP_200_OK)
