from django.contrib import admin
from .models import Client, Address, Invoice

admin.site.register(Invoice)
admin.site.register(Client)
admin.site.register(Address)

