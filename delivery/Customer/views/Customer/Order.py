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
            request.session['order_detail'] = {}
            request.session['total_price'] = 0
            request.session['number'] = 0
            return HttpResponse(status=404)

    # remove the dish order
    def post(self, request):
        request.session['order_detail']= request.data['detail']
        request.session['total_price'] = request.data['total_price']
        request.session['number'] = request.session['number'] - 1
        # https://stackoverflow.com/questions/2166856/modifying-dictionary-in-django-session-does-not-modify-session
        # request.session.modified = True
        return Response(status=status.HTTP_200_OK)

def add_orders(request):
    if request.method == 'POST':
        try:
            num = request.session['number']
            request.session['order_detail'][num] = request.data['detail']
            request.session['number'] = request.session['number'] + 1
        except:
            request.session['order_detail'] = {}
            request.session['total_price'] = 0
            request.session['number'] = 0
            return Response
