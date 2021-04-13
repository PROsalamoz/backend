from rest_framework import viewsets
from .models import Shop
from .serializers import ShopSerializers


# get, post, update, and delete
class ListAllShops(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
