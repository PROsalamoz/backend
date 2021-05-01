from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.authentication import TokenAuthentication
from .models import Product
from .serializer import ProductSerializers
from rest_framework import filters


# get, post, update, and delete
class ListAllProducts(viewsets.ModelViewSet):
    # queryset = Product.objects.filter(subcategory__category__shops_in_category__id=1)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['Title']


# class ListOrders(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializers
#
#
# class ListProductOrder(viewsets.ModelViewSet):
#     queryset = ProductOrder.objects.all()
#     serializer_class = ProductOrderSerializers
#
#
# class DeliveryPerson(viewsets.ModelViewSet):
#     queryset = Delivery_Person.objects.all()
#     serializer_class = Delivery_PersonSerializers

