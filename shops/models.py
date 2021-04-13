from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)


class ShopCategory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_category")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shop_category")

