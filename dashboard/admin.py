from django.contrib import admin
from .models import Client, Company, Address

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Address)
