from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Product, Order, ProductOrder, Delivery_Person
from .serializers import ProductSerializers, OrderSerializers, ProductOrderSerializers, Delivery_PersonSerializers


# get, post, update, and delete
class ListAllProducts(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ListOrders(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class ListProductOrder(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializers


class DeliveryPerson(viewsets.ModelViewSet):
    queryset = Delivery_Person.objects.all()
    serializer_class = Delivery_PersonSerializers
