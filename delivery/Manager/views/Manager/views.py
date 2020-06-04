from django.shortcuts import render
from .models import *

# Create your views here.
def menu_render(request):
    return #render(request, 'posts.html', {'fetch_url': '/posts/', 'is_my_post': "false"})

def historyorder_render(request):
    return #render(request, 'posts.html', {'fetch_url': '/author/myPosts/', 'is_my_post': "true"})

def deliverorder_render(request):
    return #render(request, 'otherPosts.html', {'fetch_url': '/author/posts/', 'is_my_post': "false"})

def processorder_render(request):
    return #render(request, 'posts.html', {'fetch_url': '/posts/', 'is_my_post': "false"})

def search_order_render(request):
    return 

def home(request):
    return #render(request, 'home.html', {'user_id':request.user.author.id})
