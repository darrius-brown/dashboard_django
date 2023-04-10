from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('clients/', views.ClientList.as_view(), name='client_read'),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
    #search clients by supplier
    #search invoices by client
    #search invoices by supplier
]