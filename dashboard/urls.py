from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('clients/<int:user_id>/', views.ClientListByUser.as_view(), name='client_read'),
    path('clients/<int:user_id>/<int:pk>/', views.ClientDetail.as_view(), name='client_detail'),
    path('invoices/<int:user_id>/', views.InvoiceListByUser.as_view(), name='invoice_read'),
    #search invoices by client
    #search invoices by supplier
]