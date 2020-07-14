from django.shortcuts import render
from Manager.models import Restaurant, Dish, Kind, Option, Order

# Create your views here.
def menu(request):
    return render(request, 'index.html', {'fetch_url': '/orders/processing/api/'})
