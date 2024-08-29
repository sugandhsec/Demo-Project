"""
URL configuration for ecom_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ecom_buyer_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<int:pk>', views.reset_password, name='reset_password'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('checkout/<int:val>', views.checkout, name='checkout'),
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    # path('get_data/', views.get_data, name='get_data'),
    path('check_form/', views.check_form, name='check_form'),
]
