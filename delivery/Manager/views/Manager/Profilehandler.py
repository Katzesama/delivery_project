from Manager.models import *
from Manager.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
import uuid

class UserProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Manager/editUserProfile.html'

    def get(self, request, pk, **kwargs):
        try:
            current_user_profile = Seller.objects.get(id=pk)
        except:
            return HttpResponse(status=404)

        serializer = SellerSerializer(current_user_profile)

        return Response({'serializer':serializer},  status=status.HTTP_200_OK)

    def post(self, request, pk, **kwargs):
        current_user_profile = Seller.objects.get(id=pk)
        serializer = SellerSerializer(current_user_profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Manager/editResProfile.html'

    def get(self, request, **kwargs):
        try:
            current_res_profile = Resturant.objects.all()
        except:
            return HttpResponse(status=404)

        serializer = ResSerializer(current_res_profile)

        return Response({'serializer':serializer},  status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        current_res_profile = request.user.seller.restaurant
        serializer = ResSerializer(current_res_profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("profile", current_res_profile.id)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
