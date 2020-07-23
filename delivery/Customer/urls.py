from django.urls import path, re_path
from Customer.views import views, Menu, Order
from django.contrib.auth import views as auth_view

urlpatterns = [
    #
    re_path(r'^/', views.render_menu, name='customer_menu'),
    re_path(r'^menu/', Menu.Menu.as_view(), name='customer_menu_api'),
    re_path(r'^menu/<uuid:pk>/', Menu.Dish.as_view(), name='customer_dish'),
    re_path(r'^menu/cart/', Order.Cart_Orders.as_view(), name='shopping_cart'),
    re_path(r'^menu/order/', Order.add_order, name='add_order'),
    re_path(r'^store/', views.Store.as_view(), name='store'),
    """re_path(r'^order/', name='order'),
    re_path(r'^payment/', name='payment'),
    re_path(r'^payment/success_message/', name='payment_success'),
    re_path(r'^payment/failure_message/', name='payment_fail'),
    re_path(r'^closed_message/', name='store_closed')
    """
]
