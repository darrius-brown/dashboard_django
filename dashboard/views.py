from rest_framework import generics, permissions
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]