from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer, ClientSerializer, InvoiceSerializer
from .models import Client, Invoice


class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ClientList(generics.ListCreateAPIView):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()
  permission_classes = [permissions.AllowAny]

class ClientListByUser(generics.ListCreateAPIView,):
  serializer_class = ClientSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Client.objects.filter(supplier=user_id)
        return queryset

class InvoiceListByUser(generics.ListCreateAPIView,):
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Invoice.objects.filter(supplier=user_id)
        return queryset

class InvoiceListByUserAndClient(generics.ListCreateAPIView,):
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
        user_id = self.kwargs['user_id']
        client_id = self.kwargs['client_id']
        queryset = Invoice.objects.filter(supplier=user_id, client=client_id)
        return queryset

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
  
  serializer_class = ClientSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Client.objects.filter(supplier=user_id)
        return queryset

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
  
class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Invoice.objects.filter(supplier=user_id)
        return queryset

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
  
class UserDetail(generics.RetrieveAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permission_classes = [permissions.AllowAny]



   