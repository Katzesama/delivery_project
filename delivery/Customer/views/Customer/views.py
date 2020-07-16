from django.shortcuts import render
from Manager.models import Restaurant, Dish, Kind, Option, Order
from Manager.serializer import ResSerializer, DishSerializer, KindSerializer, OptionSerializer, OrderSerializer

# Create your views here.
def render_menu(request):
    return render(request, 'index.html', {'fetch_url': '/menu/api/'})

class Store(APIView):
    def get(self, request):
            store = Restaurant.objects.all()
            serializer = ResSerializer(store)
            return Response(serializer.data, status=200)
