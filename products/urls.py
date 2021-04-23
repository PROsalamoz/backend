
from django.conf.urls import url
from django.db import router
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'products'

router = DefaultRouter()
router.register('all_products', views.ListAllProducts)
router.register('orders', views.ListOrders)
router.register('product_order', views.ListProductOrder)
router.register('Delivery_Person', views.DeliveryPerson)

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)