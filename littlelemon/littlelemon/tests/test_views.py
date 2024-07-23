from django.test import TestCase

from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializer import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Coffee", price=20, inventory=100)
        Menu.objects.create(title="Tea", price=10, inventory=100)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(str(serializer.data), "[{'id': 1, 'title': 'IceCream', 'price': '80.00', 'inventory': 100}, {'id': 2, 'title': 'Coffee', 'price': '20.00', 'inventory': 100}, {'id': 3, 'title': 'Tea', 'price': '10.00', 'inventory': 100}]")
