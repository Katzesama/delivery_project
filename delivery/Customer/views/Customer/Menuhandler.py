from Manager.models import Dish, Kind, Option
from Manager.serializer import DishSerializer, KindSerializer, OptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import status
import uuid

class Menu(APIView):
    """
    get all the dish objects and paginate them and
    return it as api to the html that renders the menu
    page (editMenu.html)
    """
    def get(self, request, **kwargs):
        menu = Dish.objects.all().order_by("kind__name")
        serializer = DishSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class A_Dish(APIView):
    """
    Retrieve, update or delete a dish instance.
    """
    def get_object(self, pk):
        try:
            return Dish.objects.get(id=pk)
        except Dish.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        dish = self.get_object(pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data, status=200)
