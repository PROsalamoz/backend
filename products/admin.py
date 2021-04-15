from django.contrib import admin

# Register your models here.
from .models import Product, Order, ProductOrder

admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
