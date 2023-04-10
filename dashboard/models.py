from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Address(models.Model):
    street = models.CharField(max_length = 100)
    suite = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 100)

    def __str__(self):
        return self.city
    
class Client(models.Model):
    supplier = models.ForeignKey(User, related_name='supplier', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date =  models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=datetime.now() + timedelta(weeks=2))

    def __str__(self, value=None):
        if value is None:
            return f"{self.client}"
        else:
            return self.client
    
