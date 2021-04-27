from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

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


@csrf_exempt
def CategoryApi(request, id=0):
    if request.method == 'GET':
        category = Category.objects.all()
        category_serializer = CategorySerializers(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)

    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializers(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(CategoryId=category_data['CategoryId'])
        category_serializer = CategorySerializers(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        category = Category.objects.get(CategoryId=id)
        category.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
