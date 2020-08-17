from django.test import Client, TestCase
from django.urls import reverse
import uuid
import json
from Manager.models import Dish, Kind, Option, Seller
from django.contrib.auth.models import User

class TestMenuHandler(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('test123')
        self.user.save()
        self.client = Client()
        self.client.login(username='testuser', password='test123')
        self.seller = Seller.objects.create(user=self.user, name='seller')

    def test_get_menu(self):
        url = reverse('menu_api')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_put_a_dish(self):
        dish = Dish.objects.create()
        kind = Kind.objects.create(name="testkind")
        url = reverse('menu_dish',args=[dish.id])
        form_data = {
        "name": "testdish",
        "price": 5.23,
        "availability": True,
        "kind": kind.id,
        }
        response = self.client.put(url, form_data , 'application/json')
        self.assertEquals(response.status_code,200)
        dish_info = json.loads(response.content)
        self.assertEquals(dish_info['name'],'testdish')
        self.assertEquals(dish_info['price'], '5.23')
        self.assertEquals(dish_info['availability'], True)
        self.assertEquals(dish_info['kind']['name'], "testkind")
