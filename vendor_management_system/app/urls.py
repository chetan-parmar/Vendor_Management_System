from django.urls import path
from .views import AcknowledgePurchaseOrderView, VendorListCreateView, VendorDetailView, VendorPerformanceView

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]