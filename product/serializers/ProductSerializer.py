from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(min_length=0)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
