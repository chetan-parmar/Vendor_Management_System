from django.db import models
from django.db.models import Count, Avg
from django.utils import timezone

class Vendor(models.Model):
    """
    Model for storing vendor information and performance metrics.
    """
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class PurchaseOrder(models.Model):
    """
    Model for capturing details of each purchase order.
    """
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    po_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"
    
    def calculate_on_time_delivery_rate(self):
        """
        Calculates and updates the on-time delivery rate for the vendor associated with this Purchase Order.
        
        The on-time delivery rate is the percentage of completed purchase orders that were delivered on time.
        """
        completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now())
        on_time_delivery_rate = (on_time_deliveries.count() / completed_pos.count()) * 100
        self.vendor.on_time_delivery_rate = on_time_delivery_rate
        self.vendor.save()

    def calculate_quality_rating_avg(self):
        """
        Calculates and updates the average quality rating for the vendor associated with this Purchase Order.
        
        The average quality rating is calculated based on completed purchase orders with a non-null quality rating.
        """
        completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed', quality_rating__isnull=False)
        quality_rating_avg = completed_pos.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
        self.vendor.quality_rating_avg = quality_rating_avg
        self.vendor.save()

    def calculate_average_response_time(self):
        """
        Calculates and updates the average response time for the vendor associated with this Purchase Order.
        
        The average response time is calculated based on completed purchase orders with a non-null acknowledgment date.
        """
        completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor, acknowledgment_date__isnull=False)
        response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos]
        
        if response_times:
            average_response_time = sum(response_times, timezone.timedelta()) / len(response_times)
            self.vendor.average_response_time = average_response_time.total_seconds() / 3600  # Convert to hours
            self.vendor.save()
    

class HistoricalPerformance(models.Model):
    """
    Model for storing historical data on vendor performance.
    """
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"Historical Performance - {self.vendor.name} - {self.date}"