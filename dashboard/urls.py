from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('clients/<int:user_id>/', views.ClientListByUser.as_view(), name='client_read'),
    path('clients/<int:user_id>/<int:pk>/', views.ClientDetail.as_view(), name='client_detail'),
    #search clients by supplier
    #search invoices by client
    #search invoices by supplier
]