from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Address, Client, Invoice
# from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.response import Response
# from rest_framework import status


UserModel = User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', "password", 'first_name', 'last_name', 'email')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = User.objects.get(id=obj['user_id'])
        return {
            'username': user.username,
            'email': user.email,
            # Add any other user information you want to include here
        }

    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     data['user'] = self.get_user(data)
    #     return data['user']['username']
    
# class MyTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         # Call the parent class's post method to obtain the token pair
#         response = super().post(request, *args, **kwargs)

#         # Add the user information to the response data
#         user = User.objects.get(id=['user_id'])
#         response.data['user'] = {
#             'username': user.username,
#             'email': user.email,
#             # Add any other user information you want to include here
#         }

#         return response


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    supplier = UserSerializer()
    
    class Meta:
        model = Client
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    supplier = UserSerializer()
    client = ClientSerializer()
    class Meta:
        model = Invoice
        fields = '__all__'

