from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Inventory, InventoryLanguage, InventoryType


class InventoryPaginationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.language = InventoryLanguage.objects.create(name="Test Language")
        self.inventory_type = InventoryType.objects.create(name="Test Type")

        # Create 5 inventory items
        for i in range(5):
            Inventory.objects.create(
                name=f"Test Inventory {i}",
                metadata={"test_key": f"test_value_{i}"},
                language=self.language,
                type=self.inventory_type,
            )

    def test_pagination_default(self):
        """Test default pagination (3 items)"""
        url = reverse("inventory-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)
        self.assertEqual(response.data["count"], 5)
        self.assertIsNotNone(response.data["next"])
        self.assertIsNone(response.data["previous"])

    def test_pagination_custom_limit(self):
        """Test custom limit"""
        url = reverse("inventory-list")
        response = self.client.get(f"{url}?limit=2")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_pagination_offset(self):
        """Test offset"""
        url = reverse("inventory-list")
        response = self.client.get(f"{url}?offset=3")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)  # Only 2 items left
        self.assertIsNone(response.data["next"])
        self.assertIsNotNone(response.data["previous"])
