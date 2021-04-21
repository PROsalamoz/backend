from django.contrib import admin

# Register your models here.
from .models import Shop, Category, SubCategory

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
