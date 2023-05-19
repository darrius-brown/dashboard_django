from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ClientSerializer, InvoiceSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Client, Invoice
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
#908213

class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CreateClient(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, user_id, format=None):
        user_id = self.kwargs['user_id']
        serializer = ClientSerializer(data=request.data, context={'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateInvoice(generics.CreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, user_id, client_id, format=None):
        user_id = self.kwargs['user_id']
        client_id = self.kwargs['client_id']
        serializer = InvoiceSerializer(data=request.data, context={'user_id': user_id, 'client_id': client_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientListByUser(generics.ListAPIView,):
  serializer_class = ClientSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Client.objects.filter(supplier=user_id)
        return queryset

class InvoiceListByUser(generics.ListAPIView,):
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Invoice.objects.filter(supplier=user_id)
        return queryset

class InvoiceListByUserAndClient(generics.ListAPIView,):
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
        user_id = self.kwargs['user_id']
        client_id = self.kwargs['client_id']
        queryset = Invoice.objects.filter(supplier=user_id, client=client_id)
        return queryset

class InvoiceListByUserAndPaid(generics.ListAPIView):
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Invoice.objects.filter(supplier=user_id, paid=True)
        return queryset

class InvoiceListByUserAndUnpaid(generics.ListAPIView):
  serializer_class = InvoiceSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Invoice.objects.filter(supplier=user_id, paid=False)
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

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username:
           return Response('Username can\'t be blank.')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid username/password'}, status=400)

        refresh = RefreshToken.for_user(user)

        data = {
            'user_id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data)

   