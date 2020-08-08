from .models import *
import uuid

def get_basic_information(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        seller = Seller.objects.get(user = request.user)
        profile_id = seller.id
        profile_img = seller.image.url if seller.image else ""
    else:
        profile_id = ""
        profile_img = ""


    return {
        'profile_id': profile_id,
        'profile_img': profile_img,
        'orders_count': Order.objects.filter(status='处理中').count()
    }
