from django.urls import path
from .. import views

urlpatterns = [
    #Basic Read Paths
    path('clients/create/<int:user_id>/', views.CreateClient.as_view(), name='create_client'),
    path('clients/<int:user_id>/', views.ClientListByUser.as_view(), name='client_read'),
    path('clients/<int:user_id>/count', views.ClientCountByUser.as_view(), name='client_count'),
    #Count Paths
    path('clients/<int:user_id>/<int:pk>/', views.ClientDetail.as_view(), name='client_detail'),
    
    
]