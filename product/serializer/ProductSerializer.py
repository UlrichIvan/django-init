from rest_framework import serializers
import uuid6 as uuid


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
