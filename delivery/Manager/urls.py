from django.urls import path, re_path
#from Manager.views
from django.contrib.auth import views as auth_view
from views.Manger import views, Menu, Orders, Profile

urlpatterns = [
    #
    re_path(r'^login/', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^home/', name='home', views.home, name='home'),

    #
    re_path(r'^userprofile/', name='uprofile', Profile.UserProfile.as_view(), name='userprofile'),
    re_path(r'^resprofile/', name='rprofile', Profile.ResProfile.as_view(), name='resprofile'),
    re_path(r'^menu/api/', Menu.Menu.as_view(), name='menu_api')
    re_path(r'^menu/', name='menu', views.menu_render, name='render_menu'),
    re_path(r'^menu/<int:pk>/', Menu.Dish.as_view(), name='menu_dish'),
    #re_path(r'^orders/',name='order_list'),
    re_path(r'^orders/processing/api/', Orders.ProceOrdersList.as_view(), name='proceorder_api'),
    re_path(r'^orders/delivery/api/', Orders.DeliverOrdersList.as_view(), name='deliverorder_api'),
    re_path(r'^orders/history/api/', Orders.HisOrdersList.as_view(), name='hisorder_api'),
    re_path(r'^orders/processing/', views.processorder_render, name='order_processing'),
    re_path(r'^orders/delivery/', views.deliverorder_render, name='order_delivering'),
    re_path(r'^orders/history/', views.historyorder_render, name='order_history'),
    re_path(r'^orders/processing/<int:pk>/', Orders.ProcessOrder.as_view(), name=''),
    re_path(r'^orders/delivery/<int:pk>/', Orders.DeliverOrder.as_view(), name='order_delivering'),
    re_path(r'^orders/history/<int:pk>/', Orders.HistoryOrder.as_view(), name='order_history')
]
