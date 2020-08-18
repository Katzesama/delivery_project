from Manager.models import Dish, Kind, Option, Order, OrderItem
from Manager.serializer import DishSerializer, KindSerializer, OptionSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from delivery import settings
import uuid
import json
from django.db.models import Q
import os
from random import Random
import time

class CartOrders(APIView):
    def get(self, request):
        try:
            order = Order.objects.get(id=request.session["order_id"])
            orderitems = OrderItem.objects.filter(order=order).order_by("num")
            detail = OrderItemSerializer(orderitems, many=True)
            total = request.session['total_price']
            return Response({'order_detail' : detail.data, 'total_price' : total, 'order_num': len(detail.data)}, status=status.HTTP_200_OK)
        except:
            request.session['total_price'] = 0
            request.session['number'] = 1
            detail = {}
            total = request.session['total_price']
            return Response({'order_detail' : detail, 'total_price' : total, 'order_num': len(detail)}, status=status.HTTP_200_OK)

    # remove the dish order
    def delete(self, request):
        try:
            data = json.loads(request.body)
            order = Order.objects.get(id=request.session["order_id"])
            orderitem = OrderItem.objects.filter(Q(order=order) & Q(num=data['key']))
            orderitem.delete()
            # https://stackoverflow.com/questions/2166856/modifying-dictionary-in-django-session-does-not-modify-session
            request.session['total_price'] = request.session['total_price'] - float(data['price'])
            order.total_price = request.session['total_price']
            order.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # checkout
    def put(self, request):
        try:
            order = Order.objects.get(id=request.session['order_id'])
            order.total_price = request.session['total_price']
            order.save()
            return Response({'id': order.id}, status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=404)

def add_order(request):
    if request.method == 'PUT':
        try:
            order_id = request.session["order_id"]
        except:
            order = Order.objects.create()
            request.session['order_id'] = str(order.id)
            request.session['total_price'] = 0
            request.session['number'] = 1
        data = json.loads(request.body)
        order = Order.objects.get(id=request.session["order_id"])
        orderitem = OrderItem.objects.create(order=order, num=request.session["number"])
        orderitem.detail = json.dumps(data)
        orderitem.save()
        request.session['total_price'] = request.session['total_price'] + float(data['price'])
        request.session['number'] = request.session['number'] + 1
        return HttpResponse(json.dumps(orderitem.id), status=status.HTTP_200_OK)



# https://blog.csdn.net/lm_is_dc/article/details/82864480
# use Django to implement wechat pay
class CheckoutOrders(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        order = self.get_object(pk)
        try:
            request.session['order_id']
        except:
            return Response("Overtime", status=200)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=200)

    def post(self, request, pk):
        order = self.get_object(pk)
        data = request.data

        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'Customer/wechatpay.html')
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        order = self.get_object(pk)
        order.payed = True
        order.save()
        # when checkout done
        try:
            del request.session['order_id']
            del request.session['order_detail']
            del request.session['total_price']
            del request.session['number']
        except:
            pass
        return Response(status=status.HTTP_200_OK)
