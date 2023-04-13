from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('clients/<int:user_id>/', views.ClientListByUser.as_view(), name='client_read'),
    path('invoices/<int:user_id>/', views.InvoiceListByUser.as_view(), name='invoice_read_by_user'),
    path('invoices/<int:user_id>/<int:client_id>/', views.InvoiceListByUserAndClient.as_view(), name='invoice_read_by_client'),
    path('clients/<int:user_id>/<int:pk>/', views.ClientDetail.as_view(), name='client_detail'),
    path('invoices/detail/<int:user_id>/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice_detail'),
    #search invoices by client
    
]