from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order, OrderTag
from interview.inventory.models import Inventory, InventoryLanguage, InventoryType


class OrderTagsListViewTests(APITestCase):
    def setUp(self):
        self.language = InventoryLanguage.objects.create(name="Test Language")
        self.inventory_type = InventoryType.objects.create(name="Test Type")
        self.inventory = Inventory.objects.create(
            name="Test Inventory",
            metadata={"test_key": "test_value"},
            language=self.language,
            type=self.inventory_type,
        )

        self.order = Order.objects.create(
            inventory=self.inventory,
            is_active=True,
            start_date="2023-01-01",
            embargo_date="2023-12-31",
        )

        self.tag1 = OrderTag.objects.create(name="Tag 1")
        self.tag2 = OrderTag.objects.create(name="Tag 2")

        self.order.tags.add(self.tag1, self.tag2)

    def test_list_order_tags(self):
        url = reverse("order-tags-list", args=[self.order.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Tag 1")
        self.assertEqual(response.data[1]["name"], "Tag 2")

    def test_list_order_tags_nonexistent_order(self):
        url = reverse("order-tags-list", args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
