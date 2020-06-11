from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .serializer import AuthorSerializer, FriendSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
import uuid


class Menu(APIView):
    """
    get all the dish objects and paginate them and
    return it as api to the html that renders the menu
    page (editMenu.html)
    """
    def get(self, request, post_id, **kwargs):
        if not request.user.is_authenticated():
            return redirect('login')
        else:
            menu = Dish.objects.all()
            pg_obj=PaginationModel()
            pg_res=pg_obj.paginate_queryset(queryset=menu, request=request)
            res=DishSerializer(instance=pg_res, many=True)
            return pg_obj.get_paginated_response(res.data)


class Dish(APIView):
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
        dish_serializer = DishSerializer(dish)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
