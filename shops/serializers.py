from rest_framework import serializers
from .models import Shop, Category, SubCategory


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'slug', 'address', 'phone', 'img', 'category']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'shops_in_category', 'bigCategory']


class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
