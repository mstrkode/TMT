from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from interview.inventory.models import (Inventory, InventoryLanguage,
                                        InventoryType)
from interview.order.models import Order


class DeactivateOrderViewTests(APITestCase):
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

    def test_deactivate_order(self):
        url = reverse("deactivate-order", args=[self.order.id])
        response = self.client.post(url)
        self.order.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.order.is_active)

    def test_deactivate_nonexistent_order(self):
        url = reverse("deactivate-order", args=[999])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class OrdersBetweenDatesViewTests(APITestCase):
    def setUp(self):
        self.language = InventoryLanguage.objects.create(name="Test Language")
        self.inventory_type = InventoryType.objects.create(name="Test Type")
        self.inventory = Inventory.objects.create(
            name="Test Inventory",
            metadata={"test_key": "test_value"},
            language=self.language,
            type=self.inventory_type
        )

        self.order1 = Order.objects.create(
            inventory=self.inventory,
            is_active=True,
            start_date='2023-01-01',
            embargo_date='2023-06-30'
        )

        self.order2 = Order.objects.create(
            inventory=self.inventory,
            is_active=True,
            start_date='2023-07-01',
            embargo_date='2023-12-31'
        )

    def test_orders_between_dates(self):
        url = reverse('orders-between-dates')
        response = self.client.get(url, {'start_date': '2023-01-01', 'embargo_date': '2023-06-30'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.order1.id)

    def test_orders_between_dates_no_results(self):
        url = reverse('orders-between-dates')
        response = self.client.get(url, {'start_date': '2024-01-01', 'embargo_date': '2024-12-31'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_orders_between_dates_missing_params(self):
        url = reverse('orders-between-dates')
        response = self.client.get(url, {'start_date': '2023-01-01'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
