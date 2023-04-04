from rest_framework import generics, permissions
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer, ClientSerializer
from .models import Client


class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ClientList(generics.ListCreateAPIView):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()
  permission_classes = [permissions.AllowAny]

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()
  permission_classes = [permissions.AllowAny]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)