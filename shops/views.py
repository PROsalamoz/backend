from rest_framework import viewsets

from .models import Shop, Category
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import ShopSerializers, CategorySerializers


@api_view(['GET'])
def index(request):
    all_shops = Shop.objects.all()
    data = ShopSerializers(all_shops, many=True).data
    return Response([data])


class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
