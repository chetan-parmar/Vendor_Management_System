from django.test import TestCase
from django.utils import timezone
from app.models import Vendor, PurchaseOrder


class PurchaseOrderModelTestCase(TestCase):
    def setUp(self):
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
            status='completed',
            quality_rating=4.5,  # Example quality rating
            issue_date=timezone.now() - timezone.timedelta(days=10),
            acknowledgment_date=timezone.now() - timezone.timedelta(days=5),
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.purchase_order),
            f"PO {self.purchase_order.po_number} - {self.vendor.name}"
        )

    def test_calculate_quality_rating_avg(self):
        # Assuming calculate_quality_rating_avg updates vendor's quality_rating_avg
        self.purchase_order.calculate_quality_rating_avg()
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.quality_rating_avg, 4.5)  # Example quality rating

    def test_calculate_average_response_time(self):
        # Assuming calculate_average_response_time updates vendor's average_response_time
        self.purchase_order.calculate_average_response_time()
        self.vendor.refresh_from_db()
        self.assertIsNotNone(self.vendor.average_response_time)
