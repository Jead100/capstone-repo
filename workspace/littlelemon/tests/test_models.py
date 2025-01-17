from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_create_menu_item(self):
        # Create a new instance of the Menu model
        menu_item = Menu.objects.create(
            title = "Cheeseburger",
            price = 9.99,
            inventory = 50
        )
        # Compare the string representation of the object with the expected value.
        self.assertEqual(str(menu_item), "Cheeseburger : 9.99")
