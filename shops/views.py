from .models import Shop
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import ShopSerializers


@api_view(['GET'])
def index(request):
    all_shops = Shop.objects.all()
    data = ShopSerializers(all_shops, many=True).data
    return Response([data])
