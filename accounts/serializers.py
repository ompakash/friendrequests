# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    full_name = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    occupation = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'full_name', 'address', 'occupation']

    def validate(self, data):
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError({"password2": "Passwords must match."})
        
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})
        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password1')
        full_name = validated_data.get('full_name', '')
        address = validated_data.get('address', '')
        occupation = validated_data.get('occupation', '')
        user = CustomUser(
            email=email,
            username=email,
            full_name=full_name,
            address=address,
            occupation=occupation
        )
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
