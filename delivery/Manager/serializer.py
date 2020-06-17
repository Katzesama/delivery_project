from .models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


# serializers
# reference: https://www.django-rest-framework.org/api-guide/serializers/
# https://docs.djangoproject.com/en/2.1/topics/serialization/
# https://www.jianshu.com/p/9e19ee78d3cc

# pagination
# reference: https://www.cnblogs.com/wdliu/p/9142832.html
# https://www.django-rest-framework.org/api-guide/pagination/

# reference: https://docs.djangoproject.com/en/2.0/ref/request-response/
# https://www.django-rest-framework.org/api-guide/fields/

class PaginationModel(PageNumberPagination):
    page_size = 10
    # Client can control the page using this query parameter.
    page_query_param = 'page'
    # Client can control the page size using this query parameter.
    page_size_query_param = 'size'
    # Set to an integer to limit the maximum page size the client may request.
    max_page_size = None

    def get_paginated_response(self, data):
        if "menu" in self.request.path:
            type = "menu"
        else:
            type = "orders"
        response_body = OrderedDict([
            ("query", type),
            ("count", self.page.paginator.count),
            ("current", self.page.number),
            ("size", self.page_size),
            ("next", self.get_next_link()),
            ("previous", self.get_previous_link()),
            (type, data)
        ])

        if self.get_previous_link() is None:
            del response_body["previous"]
        if self.get_next_link() is None:
            del response_body["next"]
        return Response(response_body)



class DishSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Dish.DISHTYPE)
    picture = serializer.ImageField(required=False)
    class Meta:
        model = Dish
        fields = "__all__"

class OpenTimeSerializer(serializers.ModelSerializer):
    weekdays = serializers.ChoiceField(choices=OpenningTime.WEEKDAYS)
    class Meta:
        model = Order
        fields = "__all__"

class ResSerializer(serializers.ModelSerializer):
    wechatcode = serializer.ImageField(required=False)
    openning_times = OpenTimeSerializer(read_only=False)
    class Meta:
        model = Restaurant
        fields = "__all__"

class SellerSerializer(serializers.ModelSerializer):
    restaurant = ResSerializer(read_only=True)
    image = serializer.ImageField(required=False)
    class Meta:
        model = Order
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Order.ORDERSTATUS)
    class Meta:
        model = Order
        fields = "__all__"
