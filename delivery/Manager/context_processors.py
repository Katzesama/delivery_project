from .models import *
import uuid

def get_basic_information(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        profile_id = request.user.seller.id
    else:
        profile_id = ""

    return {
        'profile_id': profile_id,
        'orders_number': Order.objects.filter(status='PROCESSING').count()
    }

def get_dish_types(request):
    return {
        'dish_types': ['rice', 'veg']
    }
