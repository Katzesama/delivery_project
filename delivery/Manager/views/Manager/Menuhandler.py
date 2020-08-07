from Manager.models import *
from Manager.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import uuid


class Menu(APIView):
    """
    get all the dish objects and paginate them and
    return it as api to the html that renders the menu
    page (editMenu.html)
    """
    def get(self, request, **kwargs):
        menu = Dish.objects.all().order_by('name')
        pg_obj=PaginationModel()
        pg_res=pg_obj.paginate_queryset(queryset=menu, request=request)
        res=DishSerializer(instance=pg_res, many=True)
        return pg_obj.get_paginated_response(res.data)


class A_Dish(APIView):
    """
    Retrieve, update or delete a dish instance.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Dish.objects.get(id=pk)
        except Dish.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        dish = self.get_object(pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data, status=200)

    def post(self, request, pk):
        dish = self.get_object(pk)
        data = json.loads(request.body)
        serializer = DishSerializer(dish, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        dish = self.get_object(pk)
        data = request.data
        if 'kind' in data.keys():
            kind = Kind.objects.get(id=data['kind'])
            dish.kind = kind
            dish.save()

        serializer = DishSerializer(dish, data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            try:
                del request.session['dish_id']
            except:
                pass
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dish = self.get_object(pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Dish_Kinds(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Kind.objects.get(id=pk)
        except Kind.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request):
        kinds = Kind.objects.all()
        serializer = KindSerializer(kinds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        kind = Kind.objects.create()
        data = json.loads(request.body)
        print(data)
        serializer = KindSerializer(kind, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Option_Dish(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Option.objects.get(id=pk)
        except Option.DoesNotExist:
            return HttpResponse(status=404)

    # get the option
    def get(self, request, pk):
        option = self.get_object(pk)
        serializer = OptionSerializer(option)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # edit an option
    def post():
        print("here is post")
        return Response(status=status.HTTP_200_OK)

    # create an option
    def put(self, request, pk):
        current_dish = get_object_or_404(Dish, id=pk)
        a_option = Option.objects.create(dish=current_dish)
        data = json.loads(request.body)
        serializer = OptionSerializer(a_option, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        option = self.get_object(pk)
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
