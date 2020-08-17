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

    def test_post_a_dish(self):
        kind = Kind.objects.create(name="testkind")
        dish = Dish.objects.create(name="test", price=0.00, availability=False, kind=kind)
        url = reverse('menu_dish', args=[dish.id])
        form_data = {
        "name": "testdish",
        "price": 5.23,
        "availability": True,
        }
        response = self.client.post(url, form_data , 'application/json')
        self.assertEquals(response.status_code,200)
        dish_info = json.loads(response.content)
        self.assertEquals(dish_info['name'],'testdish')
        self.assertEquals(dish_info['price'], '5.23')
        self.assertEquals(dish_info['availability'], True)
        self.assertEquals(dish_info['kind']['name'], "testkind")

    def test_del_a_dish(self):
        kind = Kind.objects.create(name="testkind")
        dish = Dish.objects.create(name="test", price=0.00, availability=False, kind=kind)
        dish_id = dish.id
        url = reverse('menu_dish', args=[dish.id])
        response = self.client.delete(url)
        self.assertEquals(response.status_code,204)
        self.assertFalse(Dish.objects.filter(pk=dish_id).exists())

    def test_put_a_kind(self):
        url = reverse('handle_kinds')
        form_data = {
        "name": "testkind",
        }
        response = self.client.put(url, form_data , 'application/json')
        self.assertEquals(response.status_code,200)
        kind_info = json.loads(response.content)
        self.assertEquals(kind_info['name'],'testkind')

    def test_put_an_option(self):
        kind = Kind.objects.create(name="testkind")
        dish = Dish.objects.create(name="testdish", price=0.00, availability=False, kind=kind)
        url = reverse('dish_option',args=[dish.id])
        form_data = {
        "detail": "testoption",
        "price": 2.33,
        }
        response = self.client.put(url, form_data , 'application/json')
        self.assertEquals(response.status_code,200)
        option_info = json.loads(response.content)
        self.assertEquals(option_info['detail'],'testoption')
        self.assertEquals(option_info['price'],'2.33')

    def test_del_an_option(self):
        kind = Kind.objects.create(name="testkind")
        dish = Dish.objects.create(name="testdish", price=0.00, availability=False, kind=kind)
        option = Option.objects.create(detail="testoption", price=2.33, dish=dish)
        option_id = option.id
        url = reverse('handle_option',args=[option.id])
        response = self.client.delete(url)
        self.assertEquals(response.status_code,204)
        self.assertFalse(Option.objects.filter(pk=option_id).exists())
