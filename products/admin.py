from django.contrib import admin
from .models import Delivery_Person, Product, ProductOrder, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
admin.site.register(Delivery_Person)