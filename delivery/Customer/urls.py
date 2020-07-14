from django.urls import path, re_path
from Customer.views import views, Menu, Order
from django.contrib.auth import views as auth_view

urlpatterns = [
    #
    re_path(r'^menu/', views.menu, name='menu'),
    re_path(r'^menu/api/', Menu.Menu.as_view(), name='menu_api'),
    """re_path(r'^order/', name='order'),
    re_path(r'^payment/', name='payment'),
    re_path(r'^payment/success_message/', name='payment_success'),
    re_path(r'^payment/failure_message/', name='payment_fail'),
    re_path(r'^closed_message/', name='store_closed')
    """
]
