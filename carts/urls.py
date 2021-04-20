from django.conf.urls import url
from django.db import router
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'carts'

router = DefaultRouter()
router.register('carts', views.ListCarts)
router.register('cartItem', views.ListCartItem)

urlpatterns = [

                  path('', include(router.urls))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
