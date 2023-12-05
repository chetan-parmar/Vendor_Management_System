from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Vendor model.

    Serializes Vendor model instances to and from JSON format.

    Attributes:
        Meta:
            model (Vendor): The Vendor model to be serialized.
            fields (list): List of fields to include in the serialized representation (all fields in this case).
    """
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorPerformanceSerializer(serializers.ModelSerializer):
    """
    Serializer class for presenting specific performance metrics of the Vendor model.

    Serializes a subset of Vendor model fields related to performance metrics.

    Attributes:
        Meta:
            model (Vendor): The Vendor model to be serialized.
            fields (list): List of fields to include in the serialized representation,
                           focusing on performance metrics such as on-time delivery rate, quality rating average,
                           average response time, and fulfillment rate.
    """
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']