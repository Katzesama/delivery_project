from django.shortcuts import render
from Manager.models import Restaurant, Dish, Kind, Option, Order
from Manager.serializer import ResSerializer, DishSerializer, KindSerializer, OptionSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import uuid

# Create your views here.
def render_menu(request):
    return render(request, 'index.html', {'fetch_url': '/menu/api/'})

class Store(APIView):
    def get(self, request):
            store = Restaurant.objects.all()
            serializer = ResSerializer(store)
            return Response(serializer.data, status=200)
