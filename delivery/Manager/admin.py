from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Seller)
admin.site.register(OpenningTime)
admin.site.register(Restaurant)
admin.site.register(Type)
admin.site.register(Dish)
admin.site.register(Order)
