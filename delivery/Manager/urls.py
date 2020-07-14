from django.urls import path, re_path
#from Manager.views
from django.contrib.auth import views as auth_view
from views.Manger import views, Menu, Orders, Profile

urlpatterns = [
    #
    re_path(r'^login/', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^home/', views.home, name='home'),

    #
    re_path(r'^userprofile/<uuid:pk>/', Profile.UserProfile.as_view(), name='userprofile'),
    re_path(r'^resprofile/', Profile.ResProfile.as_view(), name='resprofile'),
    re_path(r'^menu/api/', Menu.Menu.as_view(), name='menu_api'),
    re_path(r'^menu/', views.menu_render, name='render_menu'),
    re_path(r'^menu/new/', views.new_dish, name='new_dish'),
    re_path(r'^menu/<uuid:pk>/', Menu.Dish.as_view(), name='menu_dish'),
    #re_path(r'^orders/',name='order_list'),
    re_path(r'^orders/processing/api/', Orders.ProceOrdersList.as_view(), name='proceorder_api'),
    re_path(r'^orders/delivery/api/', Orders.DeliverOrdersList.as_view(), name='deliverorder_api'),
    re_path(r'^orders/history/api/', Orders.HisOrdersList.as_view(), name='hisorder_api'),
    re_path(r'^orders/processing/', views.processorder_render, name='proceorder'),
    re_path(r'^orders/delivery/', views.deliverorder_render, name='deliverorder'),
    re_path(r'^orders/history/', views.historyorder_render, name='hisorder'),
    re_path(r'^orders/<int:pk>/', Orders.OrderDetail.as_view(), name='order_detail'),
    #re_path(r'^orders/delivery/<int:pk>/', Orders.DeliverOrder.as_view(), name='deliverorder_detail'),
    #re_path(r'^orders/history/<int:pk>/', Orders.HistoryOrder.as_view(), name='hisorder_detail'),
    re_path(r'^orders/search/api/(?P<ordernum>.+)/$'), Order.SearchOrder.as_view(), name="search_order"),
    re_path(r'^orders/search/'), views.search_order_render, name="search_order_render")
]
