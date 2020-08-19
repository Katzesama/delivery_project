from Manager.models import *
from Manager.serializer import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import uuid
import json

class HisOrdersList(APIView):
    def get(self, request, **kwargs):
        orders = Order.objects.filter(Q(status='完成') | Q(status='已退款')).order_by('-ordered_time')
        pg_obj=PaginationModel()
        pg_res=pg_obj.paginate_queryset(queryset=orders, request=request)
        res=OrderSerializer(instance=pg_res, many=True)
        return pg_obj.get_paginated_response(res.data)


class DeliverOrdersList(APIView):
    def get(self, request, **kwargs):
        orders = Order.objects.filter(status='送餐中').order_by('-ordered_time')
        pg_obj=PaginationModel()
        pg_res=pg_obj.paginate_queryset(queryset=orders, request=request)
        res=OrderSerializer(instance=pg_res, many=True)
        return pg_obj.get_paginated_response(res.data)


class ProceOrdersList(APIView):
    def get(self, request, **kwargs):
        orders = Order.objects.filter(Q(status='处理中') | Q(status='退款中')).order_by('-ordered_time')
        pg_obj=PaginationModel()
        pg_res=pg_obj.paginate_queryset(queryset=orders, request=request)
        res=OrderSerializer(instance=pg_res, many=True)
        return pg_obj.get_paginated_response(res.data)

class OrderDetail(APIView):
    """
    Retrieve, update an order instance.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=200)

    def post(self, request, pk):
        order = self.get_object(pk)
        data = request.data
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchOrder(APIView):
    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            orders = Order.objects.filter(customer_phone=kwargs['phonenum']).order_by('-ordered_time')
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
