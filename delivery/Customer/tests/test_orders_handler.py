from django.test import Client, TestCase
from django.urls import reverse
import uuid
import json
from Manager.models import Dish, Option, Order, OrderItem
from Manager.serializer import OrderSerializer, OrderItemSerializer

class TestOrderHandler(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_an_order_item(self):
        url = reverse('add_order')
        form_data1 = {
            'quantity': '2',
            'price': '5.00',
            'options': "option1, option2, option3"
        }
        response = self.client.put(url, form_data1, 'application/json')
        self.assertEquals(response.status_code,200)
        item_id1 = json.loads(response.content)
        item_info1 = OrderItem.objects.get(id=item_id1)
        self.assertEquals(item_info1.num, 1)
        self.assertEquals(item_info1.detail, json.dumps(form_data1))

        form_data2 = {
            'quantity': '1',
            'price': '2.00',
            'options': "option1"
        }
        response = self.client.put(url, form_data2, 'application/json')
        self.assertEquals(response.status_code,200)
        item_id2 = json.loads(response.content)
        item_info2 = OrderItem.objects.get(id=item_id2)
        self.assertEquals(item_info2.num, 2)
        self.assertEquals(item_info2.detail, json.dumps(form_data2))
        self.assertEquals(item_info1.order, item_info2.order)

    def test_get_cart_order(self):
        url1 = reverse('shopping_cart')
        response = self.client.get(url1)
        self.assertEquals(response.status_code,200)
        orderitems = json.loads(response.content)
        self.assertEquals(orderitems['order_detail'], {})
        self.assertEquals(orderitems['total_price'], 0)
        self.assertEquals(orderitems['order_num'], 0)

        url2 = reverse('add_order')
        form_data = {
            'quantity': '2',
            'price': '5.00',
            'options': "option1, option2, option3"
        }
        response = self.client.put(url2, form_data, 'application/json')
        self.assertEquals(response.status_code,200)
        item_id1 = json.loads(response.content)
        item_info1 = OrderItem.objects.get(id=item_id1)

        response = self.client.get(url1)
        self.assertEquals(response.status_code,200)
        orderitems = json.loads(response.content)
        self.assertEquals(orderitems['order_detail'][0]['id'], item_info1.id)
        self.assertEquals(orderitems['total_price'], 5)
        self.assertEquals(orderitems['order_num'], 1)

    def test_delete_cart_order(self):
        url1 = reverse('add_order')
        form_data = {
            'quantity': '2',
            'price': '5.00',
            'options': "option1, option2, option3"
        }
        response = self.client.put(url1, form_data, 'application/json')
        self.assertEquals(response.status_code,200)
        item_id = json.loads(response.content)
        item_info = OrderItem.objects.get(id=item_id)

        url2 = reverse('shopping_cart')
        form_data = {
        'key': item_info.num,
        'price': 5.00
        }
        response = self.client.delete(url2, form_data, 'application/json')
        self.assertEquals(response.status_code,204)
        self.assertFalse(OrderItem.objects.filter(id=item_id).exists())
        self.assertEquals(self.client.session['total_price'], 0)
