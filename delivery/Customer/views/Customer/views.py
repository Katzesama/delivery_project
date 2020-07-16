from django.shortcuts import render
from Manager.models import Restaurant, Dish, Kind, Option, Order

# Create your views here.
def render_menu(request):
    return render(request, 'index.html', {'fetch_url': '/menu/api/'})

class Store(APIView):
    def get(self, request):
            dish = self.get_object(pk)
            dish_serializer = DishSerializer(dish)
            return Response(serializer.data, status=200)
