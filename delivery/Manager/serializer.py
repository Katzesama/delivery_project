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
        response_body = {
            "query": type,
            "count": self.page.paginator.count,
            "current": self.page.number,
            "size": self.page_size,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "total_pages": self.page.paginator.num_pages,
            type: data,
        }

        if self.get_previous_link() is None:
            del response_body["previous"]
        if self.get_next_link() is None:
            del response_body["next"]
        return Response(response_body)


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = "__all__"


class DishSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False)
    options = serializers.SerializerMethodField()
    kind = KindSerializer(read_only=True)
    class Meta:
        model = Dish
        fields = "__all__"

    def get_options(self, obj):
        options = Option.objects.filter(dish=obj)
        serializer = OptionSerializer(options, many=True)
        return serializer.data

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"
        extra_kwargs = {'dish': {'required': False}}

class SellerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Seller
        fields = "__all__"
        # https://stackoverflow.com/questions/46842120/django-rest-framework-error-userthis-field-is-required
        extra_kwargs = {'user': {'required': False}}

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class ResSerializer(serializers.ModelSerializer):
    wechatcode = serializers.ImageField(required=False)
    seller = SellerSerializer(read_only=True)
    class Meta:
        model = Restaurant
        fields = "__all__"

class OpenTimeSerializer(serializers.ModelSerializer):
    weekdays = serializers.ChoiceField(choices=OpenningTime.WEEKDAYS)
    restaurant = ResSerializer(read_only=True)
    class Meta:
        model = OpenningTime
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Order.ORDERSTATUS)
    class Meta:
        model = Order
        fields = "__all__"
