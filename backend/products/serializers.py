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
    # get discount and limited from the model method get_discount and get_limited respectively 
    # drf will check if there is a methd with the same name as the field and if it finds it it will call it
    # and return the value of the field
    # this is how the discount and limited fields are populated
    def get_discount(self,obj):
        return obj.get_discount()
    def get_limited(self,obj):
        return obj.get_limited()