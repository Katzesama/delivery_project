from django.shortcuts import render
from .models import *

# Create your views here.
def menu_render(request):
    return render(request, 'editMenu.html', {'fetch_url': '/menu/api/'})

def new_dish(request):
    return render(request, 'addDish.html')

def processorder_render(request):
    return render(request, 'orderProcessing.html', {'fetch_url': 'orders/processing/api/'})

def deliverorder_render(request):
    return #render(request, 'otherPosts.html', {'fetch_url': '/author/posts/', 'is_my_post': "false"})

def historyorder_render(request):
    return #render(request, 'posts.html', {'fetch_url': '/author/myPosts/', 'is_my_post': "true"})

def search_order_render(request):
    return

def home(request):
    return #render(request, 'home.html', {'user_id':request.user.author.id})
