from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Cart, CartItem
from .serializers import CartSerializers, CartItemSerializers


class ListCarts(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class ListCartItem(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers
