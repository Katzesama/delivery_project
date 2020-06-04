from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
import json


class OpenningTime(models.Model):

    #https://stackoverflow.com/questions/49641493/how-to-create-business-hours-via-django
    #author: Rana El-Garem
    WEEKDAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
    )

    weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100, default='No Name')
    phone = models.CharField(max_length=12)
    wechat = models.CharField(max_length=20)
    wechatcode = models.ImageField(null=True, blank=True, upload_to="wechat_code")
    description = models.CharField(max_length =100)
    openning_times = models.ManyToManyField(OpenningTime)
    image = models.ImageField(null=True, blank=True)

# Create your models here.
class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(null=True, blank=True, upload_to="profile_pics")
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

class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(..., max_digits=5, decimal_places=2)
    description = models.CharField(max_length=2000, null=True, blank=True)
    avalibility = models.BooleanField(default=False)

class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, editable=False)
    total_price = models.DecimalField(..., max_digits=6, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=2000, null=False, blank=False)
    deliver_address = models.CharField(max_length=500, null=False, blank=False)
    customer_phone = models.CharField(max_length=12, null=False, blank=False)
    customer_email = models.CharField(max_length=50, null=True, blank=False)
    ORDERSTATUS = (
        ('PROCESSING', 'PROCESSING'),
        ('DELIVERING', 'DELIVERING'),
        ('DONE', 'DONE'),
        ('REFUNDING', 'REFUNDING'),
        ('REFUNDED', 'REFUNDED'),
    )
    status = models.CharField(default ="PROCESSING", max_length=20, choices=ORDERSTATUS)
