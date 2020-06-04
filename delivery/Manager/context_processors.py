from .models import *
import uuid

def get_basic_information(request):
    return {
        'profile_id': request.user.seller.id,
        'orders_number': Order.objects.filter(status='PROCESSING').count()
    }
