# views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import PurchaseOrder, Vendor
from .serializers import VendorPerformanceSerializer, VendorSerializer

class VendorListCreateView(ListCreateAPIView):
    """
    API view for listing and creating Vendor instances.

    Inherits from ListCreateAPIView, providing GET (list) and POST (create) operations for Vendor instances.

    Attributes:
        queryset (QuerySet): The set of Vendor instances to be displayed or modified.
        serializer_class (Serializer): The serializer class for Vendor instances.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Vendor instance.

    Inherits from RetrieveUpdateDestroyAPIView, providing GET (retrieve), PUT (update), PATCH (partial update), and DELETE operations for a specific Vendor instance.

    Attributes:
        queryset (QuerySet): The set of Vendor instances to be retrieved, updated, or deleted.
        serializer_class (Serializer): The serializer class for Vendor instances.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceView(APIView):
    """
    API view for retrieving performance metrics of a specific Vendor instance.

    Inherits from APIView, providing a custom GET operation to retrieve performance metrics using VendorPerformanceSerializer.

    Methods:
        get(request, vendor_id):
            Retrieves and returns the performance metrics of the specified Vendor instance.

    Attributes:
        None
    """
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)
    

class AcknowledgePurchaseOrderView(APIView):
    """
    API view for acknowledging a Purchase Order.

    Inherits from APIView, providing a custom POST operation to acknowledge a Purchase Order and recalculate the average response time.

    Methods:
        post(request, po_id):
            Acknowledges the specified Purchase Order, updating its acknowledgment date and recalculating the average response time.

    Attributes:
        None
    """
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)

        if purchase_order.acknowledgment_date:
            return Response({"error": "Purchase Order already acknowledged"}, status=status.HTTP_400_BAD_REQUEST)

        # Update acknowledgment_date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Recalculate average_response_time
        purchase_order.calculate_average_response_time()

        return Response({"message": "Purchase Order acknowledged successfully"}, status=status.HTTP_200_OK)
