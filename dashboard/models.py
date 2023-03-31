from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length = 100)
    catchPhrase = models.CharField(max_length = 100)
    businessStatement = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

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
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 100)
    website = models.CharField(max_length = 100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
