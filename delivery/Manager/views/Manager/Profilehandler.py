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
    template_name = 'editUserProfile.html'

    def get(self, request, **kwargs):
        try:
            current_user_profile = Seller.objects.get(id = user_id)
        except:
            return HttpResponse(status=404)

        serializer = SellerSerializer(current_user_profile)

        return Response({'serializer':serializer,'profile':current_user_profile})

    def post(self, request, **kwargs):
        current_user_profile = request.user.seller
        serializer = SellerSerializer(current_user_profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("profile", current_user_profile.id)

        print(serializer.errors)
        return Response({'serializer': serializer, 'profile': current_user_profile})

class ResProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'editResProfile.html'

    def get(self, request, **kwargs):
        try:
            current_res_profile = request.user.seller.restaurant
        except:
            return HttpResponse(status=404)

        serializer = ResSerializer(current_res_profile)

        return Response({'serializer':serializer,'profile':current_res_profile})

    def post(self, request, **kwargs):
        current_res_profile = request.user.seller.restaurant
        serializer = ResSerializer(current_res_profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("profile", current_res_profile.id)

        print(serializer.errors)
        return Response({'serializer': serializer, 'profile': current_res_profile})
