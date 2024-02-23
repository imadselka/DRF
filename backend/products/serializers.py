from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    limited = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            'limited'
        ]
    def get_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()
    # same thing for other methods
    def get_limited(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_limit()