from django.shortcuts import render

# Create your views here.
def menu_render(request):
    return render(request, 'Manager/editMenu.html', {'fetch_url': '/menu/api/'})

def new_dish(request):
    return render(request, 'Manager/addDish.html')

def processorder_render(request):
    return render(request, 'Manager/orderProcessing.html', {'fetch_url': '/orders/processing/api/'})

def deliverorder_render(request):
    return render(request, 'Manager/orderDelivering.html', {'fetch_url': '/orders/delivery/api/'})

def historyorder_render(request):
    return render(request, 'Manager/orderHistory.html', {'fetch_url': '/orders/history/api/'})

def search_order_render(request, ordernum):
    return render(request, 'Manager/searchOrder.html', {'fetch_url': '/orders/search/api/'+ str(ordernum) + '/'})

def home(request):
    return render(request, 'Manager/home.html')
