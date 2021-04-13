from rest_framework import serializers
from .models import Shop, Category


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
