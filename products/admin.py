from django.contrib import admin
from .models import Product, Order, ProductOrder
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
