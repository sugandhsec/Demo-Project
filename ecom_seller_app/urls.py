from django.urls import path
from ecom_seller_app import views

urlpatterns = [
    path('', views.seller_index, name='seller_index'),
    path('seller_register/', views.seller_register, name='seller_register'),
]
