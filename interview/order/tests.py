from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order, OrderTag
from interview.inventory.models import Inventory, InventoryLanguage, InventoryType


class TagOrdersListViewTests(APITestCase):
    def setUp(self):
        self.language = InventoryLanguage.objects.create(name="Test Language")
        self.inventory_type = InventoryType.objects.create(name="Test Type")
        self.inventory = Inventory.objects.create(
            name="Test Inventory",
            metadata={"test_key": "test_value"},
            language=self.language,
            type=self.inventory_type,
        )

        self.order1 = Order.objects.create(
            inventory=self.inventory,
            is_active=True,
            start_date="2023-01-01",
            embargo_date="2023-06-30",
        )

        self.order2 = Order.objects.create(
            inventory=self.inventory,
            is_active=True,
            start_date="2023-07-01",
            embargo_date="2023-12-31",
        )

        self.tag = OrderTag.objects.create(name="Test Tag")

        self.order1.tags.add(self.tag)
        self.order2.tags.add(self.tag)

    def test_list_tag_orders(self):
        url = reverse("tag-orders-list", args=[self.tag.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], self.order1.id)
        self.assertEqual(response.data[1]["id"], self.order2.id)

    def test_list_tag_orders_nonexistent_tag(self):
        url = reverse("tag-orders-list", args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
