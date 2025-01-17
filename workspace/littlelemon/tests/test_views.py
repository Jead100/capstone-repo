from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
# Import the Menu model and serializer
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
# Import User model and Token model for authentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(title="Cheeseburger", price = 9.99, inventory = 50)
        Menu.objects.create(title="Margherita Pizza", price = 12.99, inventory = 30)
        Menu.objects.create(title="Caesar Salad", price = 8.99, inventory = 20)

        # Create a test user and generate a token for authentication
        self.user = User.objects.create_user(username='testuser123', password='testpassword123')
        self.token = Token.objects.create(user=self.user)

        # Initialize the APIClient and set the authentication token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get(reverse('menu-list'))

        # Serialize the Menu objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that the serialized data equals the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)