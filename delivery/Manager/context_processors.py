from .models import *
import uuid

def get_basic_information(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        seller = Seller.objects.get(user = request.user)
        profile_id = seller.id
        profile_img = seller.image
    else:
        profile_id = ""
        profile_img = ""

    return {
        'profile_id': profile_id,
        'profile_img': profile_img,
        'orders_number': Order.objects.filter(status='PROCESSING').count()
    }

def get_dish_types(request):
    return {
        'dish_types': ['rice', 'veg']
    }
