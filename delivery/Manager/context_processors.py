from .models import *
import uuid

def get_basic_information(request):
    profile_id = request.user.seller.id if request.user.is_authenticated else ""
    return {
        'profile_id': profile_id,
        'orders_number': Order.objects.filter(status='PROCESSING').count()
    }

def get_dish_types(request):
    return {
        'dish_types': ['rice', 'veg']
    }
