"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.db import router
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'shops'

router = DefaultRouter()
router.register('', views.ListAllShops)
# router.register('ShopCategory', views.View_ShopCategory)
# router.register('subcategory', views.SubCategory)
# router.register('category', views.Category)

urlpatterns = [url(r'^SaveFile$', views.SaveFile),
               url(r'^category/$', views.CategoryApi),
               url(r'^category/([0-9]+)$', views.CategoryApi),
               path('', include(router.urls))
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
