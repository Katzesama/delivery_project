from .models import *
import uuid

def get_basic_information(request):
    return {
        'profile_id': request.user.seller.id,
        'orders_number': Order.objects.filter(status='PROCESSING').count()
    }

def get_dish_types(request):
    return {
        'dish_types': ['rice', 'veg']
    }
