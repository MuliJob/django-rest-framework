"""Models Serializers"""
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer
    """
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        """
        Class Meta
        """
        model = Product
        fields = ['pk', 'title', 'content', 'price', 'sale_price', 'discount']

    def get_discount(self, obj):
        """
        Changing discount field
        """
        return obj.get_discount()
