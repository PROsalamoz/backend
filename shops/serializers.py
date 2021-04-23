from rest_framework import serializers
from .models import Shop, Category, SubCategory, ShopCategory


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ShopCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = '__all__'

class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
