from Manager.models import Dish, Kind, Option, Order
from Manager.serializer import DishSerializer, KindSerializer, OptionSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import uuid
import json

class CartOrders(APIView):
    def get(self, request):
        try:
            detail = request.session['order_detail']
            total = request.session['total_price']
            print(detail)
            return Response({'order_detail' : detail, 'total_price' : total, 'order_num': len(detail.keys())}, status=status.HTTP_200_OK)
        except:
            request.session['order_detail'] = {}
            request.session['total_price'] = 0
            request.session['number'] = 0
            detail = request.session['order_detail']
            total = request.session['total_price']
            return Response({'order_detail' : detail, 'total_price' : total, 'order_num': len(detail.keys())}, status=status.HTTP_200_OK)

    # remove the dish order
    def delete(self, request):
        data = json.loads(request.body)
        print(data)
        request.session['order_detail'].pop(data['key'], None)
        # https://stackoverflow.com/questions/2166856/modifying-dictionary-in-django-session-does-not-modify-session
        request.session.modified = True
        request.session['total_price'] = request.session['total_price'] - float(data['price'])
        return Response(status=status.HTTP_200_OK)

    # checkout
    def put(self, request):
        try:
            order = Order.objects.get(id=request.session['order_id'])
        except:
            order = Order()
            # detail: name quantity price options
            # i.e. {1: {'name': 'k', 'quantity': '1', 'price' : '20', 'options' : 'coke beer'}}
        detail = []
        for key, item in request.session['order_detail'].items():
            a = []
            a.append(item['name'])
            a.append(item['quantity'])
            a.append(item['price'])
            a.append(item['options'])
            detail.append(a)
        order.detail = json.dumps(detail)
        order.total_price = request.session['total_price']
        order.save()
        orderid = str(order.id)
        request.session['order_id'] = order.id
        return Response({'id': orderid}, status=status.HTTP_200_OK)

def add_order(request):
    if request.method == 'PUT':
        try:
            set_order(request)
        except:
            request.session['order_detail'] = {}
            request.session['total_price'] = 0
            request.session['number'] = 0
            set_order(request)
        return HttpResponse(status=status.HTTP_200_OK)

def set_order(request):
    data = json.loads(request.body)
    num = request.session['number']
    request.session['order_detail'][num] = data
    request.session.modified = True
    request.session['total_price'] = request.session['total_price'] + float(data['price'])
    request.session['number'] = request.session['number'] + 1

class CheckoutOrders(APIView):
    def get(self, request, pk):
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk):
        # when checkout done
        del request.session['order_id']
        del request.session['order_detail']
        del request.session['total_price']
        del request.session['number']
        return Response(status=status.HTTP_200_OK)
