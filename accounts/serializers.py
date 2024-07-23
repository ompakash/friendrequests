# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        

        if password1 != password2:
            raise serializers.ValidationError({"password2": "Passwords must match."})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})
        return data

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password1']
        user = User.objects.create_user(username=email, email=email, password=password)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
