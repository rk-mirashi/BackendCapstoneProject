from django.test import TestCase,Client
from django.urls import reverse
from restaurant.models import Menu
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.burger = Menu.objects.create(Title='Burger', Price=8.99, Inventory=5)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = Menu.objects.all()
        
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)