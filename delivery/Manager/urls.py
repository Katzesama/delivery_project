from django.urls import path, re_path
#from Manager.views
from django.contrib.auth import views as auth_views
from Manager.views.Manager import views, Menuhandler, Ordershandler, Profilehandler

urlpatterns = [
    re_path(r'^login/', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^home/', views.home, name='home'),

    re_path(r'^userprofile/(?P<pk>[0-9a-f-]+)/api/$', Profilehandler.UserProfile.as_view(), name='user_profile_api'),
    re_path(r'^userprofile/(?P<pk>[0-9a-f-]+)/$', views.user_profile_render, name='user_profile'),
    re_path(r'^resprofile/api/', Profilehandler.ResProfile.as_view(), name='resprofile_api'),
    re_path(r'^resprofile/', views.res_profile_render, name='resprofile'),

    re_path(r'^menu/api/', Menuhandler.Menu.as_view(), name='menu_api'),
    re_path(r'^menu/(?P<pk>[0-9a-f-]+)/$', Menuhandler.A_Dish.as_view(), name='menu_dish'),
    re_path(r'^menu/new/', views.new_dish, name='new_dish'),
    re_path(r'^menu/', views.menu_render, name='render_menu'),
    #re_path(r'^orders/',name='order_list'),
    re_path(r'^orders/processing/api/', Ordershandler.ProceOrdersList.as_view(), name='proceorder_api'),
    re_path(r'^orders/delivery/api/', Ordershandler.DeliverOrdersList.as_view(), name='deliverorder_api'),
    re_path(r'^orders/history/api/', Ordershandler.HisOrdersList.as_view(), name='hisorder_api'),
    re_path(r'^orders/processing/', views.processorder_render, name='proceorder'),
    re_path(r'^orders/delivery/', views.deliverorder_render, name='deliverorder'),
    re_path(r'^orders/history/', views.historyorder_render, name='hisorder'),
    re_path(r'^orders/(?P<ordernum>\d+)/$', Ordershandler.OrderDetail.as_view(), name='order_detail'),
    re_path(r'^orders/search/api/(?P<ordernum>\d+)/$', Ordershandler.SearchOrder.as_view(), name="search_order"),
    re_path(r'^orders/search/(?P<ordernum>\d+)/$', views.search_order_render, name="search_order_render"),
]
