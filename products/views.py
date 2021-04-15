from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Product, Order, ProductOrder
from .serializer import ProductSerializers, OrderSerializers, ProductOrderSerializers


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

