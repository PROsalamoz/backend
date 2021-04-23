from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Delivery_Person, Product, Order, ProductOrder
from .serialzers import Delivery_PersonSerializers, ProductSerializers, OrderSerializers, ProductOrderSerializers


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
