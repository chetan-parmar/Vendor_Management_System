# views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Vendor
from .serializers import VendorSerializer

class VendorListCreateView(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
