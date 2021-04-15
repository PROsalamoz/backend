from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Delivery_Person
from .serialzers import Delivery_PersonSerializers


class DeliveryPerson(viewsets.ModelViewSet):
    queryset = Delivery_Person.objects.all()
    serializer_class = Delivery_PersonSerializers
