from django.urls import path, re_path
from Customer.views.Customer import views, Menuhandler, Orderhandler
from django.contrib.auth import views as auth_view

urlpatterns = [
    re_path(r'^/', views.render_menu, name='customer_menu'),
    re_path(r'^menu/', Menuhandler.Menu.as_view(), name='customer_menu_api'),
    re_path(r'^menu/<uuid:pk>/', Menuhandler.Dish.as_view(), name='customer_dish'),
    re_path(r'^store/', views.Store.as_view(), name='store'),
    re_path(r'^menu/cart/', Orderhandler.CartOrders.as_view(), name='shopping_cart'),
    re_path(r'^menu/order/', Orderhandler.add_order, name='add_order'),
    re_path(r'^order/<int:pk>/', Orderhandler.CheckoutOrders.as_view(), name='checkout'),
]
