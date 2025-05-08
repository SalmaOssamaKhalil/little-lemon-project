from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

 

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test data
        self.item1 = Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        self.item2 = Menu.objects.create(title="Pasta", price=9.99, inventory=15)

 

    def test_get_all_menu_items(self):
        response = self.client.get('/menu/')  # Ensure this matches your URL
        # Fetch and serialize data for comparison
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)