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

class Cart_Orders(APIView):
    def get(self, request):
        try:
            detail = request.session['order_detail']
            total = request.session['total_price']
            return Response({'order_detail' : detail, 'total_price' : total}, status=status.HTTP_200_OK)
        except:
            request.session['order_detail'] = []
            request.session['total_price'] = 0
            return HttpResponse(status=404)

    def post(self, request):
        request.session['order_detail']= request.data['detail']
        request.session['total_price'] = request.data['total_price']
        return Response(status=status.HTTP_200_OK)

def add_orders(request):
    if request.method == 'POST':
        try:
            request.session['order_detail'] = request.session['order_detail'].append(request.data['detail'])
        except:
            request.session['order_detail'] = []
            request.session['total_price'] = 0
            return Response
