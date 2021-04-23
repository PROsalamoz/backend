from django.contrib import admin
# Register your models here.
from .models import Shop, Category,SubCategory, ShopCategory
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ShopCategory)