from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Address, Client, Invoice

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

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email')

class ClientForInvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'name')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    supplier = SupplierSerializer()
    
    #my new create
    def create (self, validated_data):
        address_data = validated_data.pop('address')
        user_data = validated_data.pop('supplier')
        user_id = self.context.get('user_id')
        
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        user = User.objects.get(id=user_id)

        client = Client.objects.create(
            address=address, 
            supplier=user, 
            **validated_data)
        
        return client

    class Meta:
        model = Client
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    client = ClientForInvoiceSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('supplier')
        client_data = validated_data.pop('client')
        user_id = self.context.get('user_id')
        client_id = self.context.get('client_id')

        user = User.objects.get(id=user_id)
        client = Client.objects.get(id=client_id)

        invoice = Invoice.objects.create(
            client=client, 
            supplier=user, 
            **validated_data)
        
        return invoice
    
    def update(self, instance, validated_data):
        supplier_data = validated_data.pop('supplier', None)
        client_data = validated_data.pop('client', None)

        instance = super().update(instance, validated_data)

        if supplier_data is not None:
            supplier_serializer = self.fields['supplier']
            supplier_instance = instance.supplier
            supplier_instance = supplier_serializer.update(supplier_instance, supplier_data)
            instance.supplier = supplier_instance

        if client_data is not None:
            client_serializer = self.fields['client']
            client_instance = instance.client
            client_instance = client_serializer.update(client_instance, client_data)
            instance.client = client_instance

        instance.save()
        return instance

    class Meta:
        model = Invoice
        fields = ('supplier', 'client', 'amount', 'paid', 'due_date')
