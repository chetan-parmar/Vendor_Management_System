from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.utils import timezone
from app.models import Vendor, PurchaseOrder


class VendorAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test client and authenticate with the token
        self.client = APIClient()
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Create some test data
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Test Contact",
            address="Test Address",
            vendor_code="V001",
        )
        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            po_number="PO001",
            order_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=7),
            items='{"item": "Test Item"}',
            quantity=10,
            status='pending',
            issue_date=timezone.now(),
        )

    def test_vendor_list_create_view(self):
        url = reverse('vendor-list-create')
        data = {
            "name": "New Vendor",
            "contact_details": "New Contact",
            "address": "New Address",
            "vendor_code": "V002",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_vendor_detail_view(self):
        url = reverse('vendor-detail', args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.vendor.name)

    def test_vendor_performance_view(self):
        url = reverse('vendor-performance', args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions for the response data as needed

    def test_acknowledge_purchase_order_view(self):
        url = reverse('acknowledge-purchase-order', args=[self.purchase_order.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions for the response data as needed
