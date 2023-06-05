from django.urls import path
from . import views
from .views import LoginView



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.CreateUser.as_view()),
    path('clients/create/<int:user_id>/', views.CreateClient.as_view(), name='create_client'),
    path('invoices/create/<int:user_id>/<int:client_id>/', views.CreateInvoice.as_view(), name='create_invoice'),
    path('clients/<int:user_id>/', views.ClientListByUser.as_view(), name='client_read'),
    path('invoices/<int:user_id>/', views.InvoiceListByUser.as_view(), name='invoice_read_by_user'),
    path('invoices/<int:user_id>/<int:client_id>/', views.InvoiceListByUserAndClient.as_view(), name='invoice_read_by_client'),
    path('invoices/<int:user_id>/paid/', views.InvoiceListByUserAndPaid.as_view(), name='invoice_read_by_client'),
    path('invoices/<int:user_id>/unpaid/', views.InvoiceListByUserAndUnpaid.as_view(), name='invoice_read_by_client'),
    path('invoices/<int:user_id>/unpaid/count', views.InvoiceCountByUserAndUnpaid.as_view(), name='invoice_count_by_client'),
    path('clients/<int:user_id>/<int:pk>/', views.ClientDetail.as_view(), name='client_detail'),
    path('invoices/detail/<int:user_id>/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice_detail'), 
    
]