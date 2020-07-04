from django.shortcuts import render
from .models import *

# Create your views here.
def menu_render(request):
    return render(request, 'editMenu.html', {'fetch_url': '/menu/api/'})

def new_dish(request):
    return render(request, 'addDish.html')

def processorder_render(request):
    return render(request, 'orderProcessing.html', {'fetch_url': '/orders/processing/api/'})

def deliverorder_render(request):
    return render(request, 'orderDelivering.html', {'fetch_url': '/orders/delivery/api/'})

def historyorder_render(request, ordernum):
    return render(request, 'orderHistory.html', {'fetch_url': '/orders/history/api/' + str(ordernum) + '/'})

def search_order_render(request):
    return render(request, )

def home(request):
    return render(request, 'home.html', {'user_id':request.user.author.id})
