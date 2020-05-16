from django.urls import path, re_path
from Manager.views import
from django.contrib.auth import views as auth_view

urlpatterns = [
    #
    re_path(r'^login/', name='login'),
    re_path(r'^logout/', name='logout'),
    re_path(r'^home/', name='home'),

    #
    re_path(r'^profile/', name='profile'),
    re_path(r'^menu/<page>/', name='menu'),
    re_path(r'^orders/', name='order_list'),
    re_path(r'^orders/waitlist', name='order_processing'),
    re_path(r'^orders/delivery', name='order_delivering'),
    re_path(r'^orders/history', name='order_history'),
