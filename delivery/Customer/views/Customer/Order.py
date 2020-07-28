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

class CartOrders(APIView):
    def get(self, request):
        try:
            detail = request.session['order_detail']
            total = request.session['total_price']
            return Response(json.dumps({'order_detail' : detail, 'total_price' : total}), status=status.HTTP_200_OK)
        except:
            request.session['order_detail'] = {}
            request.session['total_price'] = 0
            request.session['number'] = 0
            return HttpResponse(status=404)

    # remove the dish order
    def post(self, request):
        try:
            request.session['order_detail'].pop(json.loads(request.data), None)
            # https://stackoverflow.com/questions/2166856/modifying-dictionary-in-django-session-does-not-modify-session
            request.session.modified = True
            request.session['total_price'] = request.data['total_price']
            return Response(status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=404)

    # checkout
    def put(self, request):
        try:
            order = Order()
            # detail: name quantity price options
            # i.e. {1: {'name': 'k', 'quantity': '1', 'price' : '20', 'options' : 'coke beer'}}
            detail = []
            for item in request.session['order_detail']:
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
            return Response(json.dumps({'id': orderid}), status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=404)

def add_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            num = request.session['number']
            request.session['order_detail'][num] = data
            request.session.modified = True
            request.session['total_price'] = request.session['total_price'] + float(data['price'])
            request.session['number'] = request.session['number'] + 1
        except:
            request.session['order_detail'] = {}
            request.session['total_price'] = 0
            request.session['number'] = 0
            return Response(status=status.HTTP_200_OK)

class CheckoutOrders(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
