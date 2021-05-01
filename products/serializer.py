from rest_framework import serializers
from .models import Product
from shops.models import SubCategory


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'Title', 'price', 'description', 'slug', 'img', 'stock', 'subcategory']

#
# class OrderSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['code', 'description', 'slug', 'product_ordered']
#
#
# class ProductOrderSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ProductOrder
#         fields = '__all__'
#
#
# class Delivery_PersonSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Delivery_Person
#         fields = '__all__'
