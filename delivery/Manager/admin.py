from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(OpenningTime)
admin.site.register(Restaurant)
admin.site.register(Seller)
admin.site.register(Kind)
admin.site.register(Dish)
admin.site.register(Option)
admin.site.register(Order)
