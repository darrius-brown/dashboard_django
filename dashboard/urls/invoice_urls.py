from django.urls import path
from .. import views
from ..views import LoginView

urlpatterns = [
    # Basic Read Routes
    path('invoices/<int:user_id>/', views.InvoiceListByUser.as_view(), name='invoice_read_by_user'),
    path('invoices/<int:user_id>/<int:client_id>/', views.InvoiceListByUserAndClient.as_view(), name='invoice_read_by_client'),
    path('invoices/create/<int:user_id>/<int:client_id>/', views.CreateInvoice.as_view(), name='create_invoice'),
    path('invoices/<int:user_id>/paid/', views.InvoiceListByUserAndPaid.as_view(), name='invoice_read_by_client'),
    path('invoices/<int:user_id>/unpaid/', views.InvoiceListByUserAndUnpaid.as_view(), name='invoice_read_by_client'),
    path('invoices/detail/<int:user_id>/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice_detail'), 
    #Count Routes
    path('invoices/<int:user_id>/count', views.InvoiceCountByUser.as_view(), name='invoice_count_by_user'),
    path('invoices/<int:user_id>/<int:client_id>/count', views.InvoiceCountByUserAndClient.as_view(), name='invoice_count_by_client'),
    path('invoices/<int:user_id>/unpaid/count', views.InvoiceCountByUserAndUnpaid.as_view(), name='invoice_count_by_client'),
    path('invoices/<int:user_id>/paid/count', views.InvoiceCountByUserAndPaid.as_view(), name='invoice_count_by_client'),
    #Sum Routes
    path('invoices/<int:user_id>/unpaid/sum', views.InvoiceSumByUserAndUnpaid.as_view(), name='invoice_sum_by_client'),
    path('invoices/<int:user_id>/paid/sum', views.InvoiceSumByUserAndPaid.as_view(), name='invoice_sum_by_client'),
]