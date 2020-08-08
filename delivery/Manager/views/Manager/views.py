from django.shortcuts import render, redirect
from Manager.models import Dish

# Create your views here.
def user_profile_render(request, pk):
    return render(request, 'Manager/editUserProfile.html')

def res_profile_render(request):
    return render(request, 'Manager/editResProfile.html', {'fetch_url': './api/'})

def create_new_dish(request):
    try:
        dish_id = request.session['dish_id']
    except:
        dish = Dish.objects.create()
        dish_id = dish.id
        request.session['dish_id'] = str(dish_id)
    return redirect('new_dish', dish_id)

def new_dish(request, pk):
    return render(request, 'Manager/addDish.html', {'dish_id': pk})

def menu_render(request):
    return render(request, 'Manager/editMenu.html', {'fetch_url': './api/'})


def processorder_render(request):
    return render(request, 'Manager/orderProcessing.html', {'fetch_url': './api/'})

def deliverorder_render(request):
    return render(request, 'Manager/orderDelivering.html', {'fetch_url': './api/'})

def historyorder_render(request):
    return render(request, 'Manager/orderHistory.html', {'fetch_url': './api/'})

def search_order_render(request, ordernum):
    return render(request, 'Manager/searchOrder.html', {'fetch_url': '/orders/search/api/'+ str(ordernum) + '/'})

def home(request):
    return render(request, 'Manager/home.html')
