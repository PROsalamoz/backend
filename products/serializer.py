from rest_framework import serializers
from .models import Product, Order, ProductOrder


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['code', 'description', 'slug', 'product_ordered']


class ProductOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'