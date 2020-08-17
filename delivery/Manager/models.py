from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal
import uuid
import json

# Create your models here.
class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(default="", null=True, blank=True, upload_to="profile_pics/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ for Python 2
        return self.name

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100, default='No Name')
    phone = models.CharField(max_length=20)
    wechat = models.CharField(max_length=100)
    wechatcode = models.ImageField(default="", null=True, blank=True, upload_to="wechat_code/")
    description = models.CharField(max_length =100, null=True, blank=True)
    image = models.ImageField(default="", null=True, blank=True, upload_to='res_pics/')
    open = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, null=True, blank=True, on_delete=models.SET_NULL)

"""
IMPORTANT:
can be used later if the oppening time is needed
"""
class OpenningTime(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, editable=False)
    #https://stackoverflow.com/questions/49641493/how-to-create-business-hours-via-django
    #author: Rana El-Garem
    WEEKDAYS = (
    (1, "星期一"),
    (2, "星期二"),
    (3, "星期三"),
    (4, "星期四"),
    (5, "星期五"),
    (6, "星期六"),
    (7, "星期天"),
    )

    weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Kind(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)

class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(default="", null=True, blank=True, upload_to="dish_images/")
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    availability = models.BooleanField(default=True)
    kind = models.ForeignKey(Kind, null=True, blank=True, on_delete=models.SET_NULL)

class Option(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, editable=False)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    detail = models.CharField(max_length=200, blank=False, null=False, default=u'选项')
    # store the list in JSON
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    ordered_time = models.DateTimeField(auto_now_add=True)
    #store list of dish name quantity price options (eg. '[["煲仔饭",  "x1",  "$15.00", "啤酒"], ["煲仔饭",  "1",  "15.00", "啤酒"]]')
    detail = models.CharField(max_length=2000, null=True, blank=False)
    deliver_address = models.CharField(max_length=500, null=True, blank=True, default="")
    customer_phone = models.CharField(max_length=12, null=True, blank=True, default="")
    customer_email = models.CharField(max_length=50, null=True, blank=True, default="")
    order_num = models.CharField(max_length=32, null=True, blank=True, default="")
    ORDERSTATUS = (
        ('处理中', '处理中'),
        ('送餐中', '送餐中'),
        ('完成', '完成'),
        ('退款中', '退款中'),
        ('已退款', '已退款'),
    )
    payed = models.BooleanField(default=False)
    status = models.CharField(default ="处理中", max_length=100, choices=ORDERSTATUS)
