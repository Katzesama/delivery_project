from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
import json


class OpenningTime(models.Model):

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

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100, default='No Name')
    phone = models.CharField(max_length=12)
    wechat = models.CharField(max_length=20)
    wechatcode = models.ImageField(null=True, blank=True, upload_to="wechat_code/")
    description = models.CharField(max_length =100)
    openning_times = models.ManyToManyField(OpenningTime)
    image = models.ImageField(null=True, blank=True)
    open = models.BooleanField(default=True)

# Create your models here.
class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(null=True, blank=True, upload_to="profile_pics/")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ for Python 2
        return self.name

"""class Images(models.Model):
	associated_post = models.ForeignKey(Post, on_delete=models.CASCADE)
	img = models.ImageField(null=True, blank=True)

class Image(models.Model):
    image = models.TextField()
    id = models.AutoField(primary_key=True)
"""


class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(default='static/Manager/images/defaultimage.jpg', upload_to="dish_images/")
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(..., max_digits=5, decimal_places=2)
    description = models.CharField(max_length=2000, null=True, blank=True)
    availability = models.BooleanField(default=True)

    DISHTYPE = (
        ('rice', '饭'),
        ('veg', '菜'),
        ('drink', '饮料'),
    )
    type = models.CharField(default ='饭', max_length=100, choices=DISHTYPE)


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, editable=False)
    total_price = models.DecimalField(..., max_digits=6, decimal_places=2)
    ordered_time = models.DateTimeField(auto_now_add=True)
    #store list of dish name, quantity, price (eg. ["rice", "2", "5.00"])
    detail = models.CharField(max_length=2000, null=False, blank=False)
    deliver_address = models.CharField(max_length=500, null=False, blank=False)
    customer_phone = models.CharField(max_length=12, null=False, blank=False)
    customer_email = models.CharField(max_length=50, null=True, blank=True)
    order_num = models.IntegerField(unique=False)
    ORDERSTATUS = (
        ('处理中', '处理中'),
        ('送餐中', '送餐中'),
        ('完成', '完成'),
        ('退款中', '退款中'),
        ('已退款', '已退款'),
    )
    status = models.CharField(default ="处理中", max_length=100, choices=ORDERSTATUS)
