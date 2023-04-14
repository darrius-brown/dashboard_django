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
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    supplier = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    supplier = models.ForeignKey(User, related_name='invoice', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    create_date =  models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=datetime.now() + timedelta(weeks=2))

    def __str__(self, value=None):
        if value is None:
            return f"{self.client}"
        else:
            return self.client
    
