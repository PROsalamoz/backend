from rest_framework import viewsets

from .models import Shop, Category, SubCategory, ShopCategory
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import ShopSerializers, CategorySerializers, ShopCategorySerializers, SubCategorySerializers


# get, post, update, and delete
class ListAllShops(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers


class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class View_ShopCategory(viewsets.ModelViewSet):
    queryset = ShopCategory.objects.all()
    serializer_class = ShopCategorySerializers


class SubCategory(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers
